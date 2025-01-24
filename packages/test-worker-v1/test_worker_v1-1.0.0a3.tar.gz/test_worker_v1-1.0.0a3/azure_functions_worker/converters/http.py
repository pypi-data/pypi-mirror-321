# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import logging
import sys
import typing
from http.cookies import SimpleCookie

import azure.functions as func
from azure.functions import HttpRequest, HttpResponse
from . import meta


class HttpResponseConverter(meta.OutConverter, binding='http'):

    @classmethod
    def check_output_type_annotation(cls, pytype: type) -> bool:
        return (type(pytype) is type(HttpResponse)
                or issubclass(pytype, str))

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        if isinstance(obj, str):
            return meta.Datum(type='string', value=obj)

        if type(obj.__class__) is type(HttpResponse):
            status = obj.status_code
            headers = obj.headers

            if 'content-type' not in headers:
                if obj.mimetype.startswith('text/'):
                    ct = f'{obj.mimetype}; charset={obj.charset}'
                else:
                    ct = f'{obj.mimetype}'
                headers['content-type'] = ct

            body = obj.get_body()
            if body is not None:
                datum_body = meta.Datum(type='bytes', value=body)
            else:
                datum_body = meta.Datum(type='bytes', value=b'')

            cookies = None

            if "Set-Cookie" in headers:
                cookies = [SimpleCookie(cookie) for cookie in
                           headers.get_all('Set-Cookie')]
                headers.pop("Set-Cookie")

            return meta.Datum(
                type='http',
                value=dict(
                    status_code=meta.Datum(type='string', value=str(status)),
                    headers={
                        n: meta.Datum(type='string', value=h)
                        for n, h in headers.items()
                    },
                    cookies=cookies,
                    body=datum_body,
                )
            )

        raise NotImplementedError


class HttpRequestConverter(meta.InConverter,
                           binding='httpTrigger', trigger=True):

    @classmethod
    def check_input_type_annotation(cls, pytype: type) -> bool:
        return type(pytype) is type(HttpRequest)

    @classmethod
    def decode(cls, data: meta.Datum, *,
               trigger_metadata) -> typing.Any:
        if data.type != 'http':
            raise NotImplementedError

        val = data.value

        return HttpRequest(
            method=val['method'].value,
            url=val['url'].value,
            headers={n: v.value for n, v in val['headers'].items()},
            params={n: v.value for n, v in val['query'].items()},
            route_params={n: v.value for n, v in val['params'].items()},
            body_type=val['body'].type,
            body=val['body'].value,
        )

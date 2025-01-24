# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import typing
import json
from importlib import import_module

from azure.functions import OrchestrationContext, EntityContext
from . import meta


# Utilities
def _serialize_custom_object(obj):
    """Serialize a user-defined object to JSON.
    This function gets called when `json.dumps` cannot serialize
    an object and returns a serializable dictionary containing enough
    metadata to recontrust the original object.
    Parameters
    ----------
    obj: Object
        The object to serialize
    Returns
    -------
    dict_obj: A serializable dictionary with enough metadata to reconstruct
              `obj`
    Exceptions
    ----------
    TypeError:
        Raise if `obj` does not contain a `to_json` attribute
    """
    # 'safety' guard: raise error if object does not
    # support serialization
    if not hasattr(obj, "to_json"):
        raise TypeError(f"class {type(obj)} does not expose a `to_json` "
                        "function")
    # Encode to json using the object's `to_json`
    obj_type = type(obj)
    return {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__,
        "__data__": obj_type.to_json(obj)
    }


def _deserialize_custom_object(obj: dict) -> object:
    """Deserialize a user-defined object from JSON.
    Deserializes a dictionary encoding a custom object,
    if it contains class metadata suggesting that it should be
    decoded further.
    Parameters:
    ----------
    obj: dict
        Dictionary object that potentially encodes a custom class
    Returns:
    --------
    object
        Either the original `obj` dictionary or the custom object it encoded
    Exceptions
    ----------
    TypeError
        If the decoded object does not contain a `from_json` function
    """
    if ("__class__" in obj) and ("__module__" in obj) and ("__data__" in obj):
        class_name = obj.pop("__class__")
        module_name = obj.pop("__module__")
        obj_data = obj.pop("__data__")

        # Importing the clas
        module = import_module(module_name)
        class_ = getattr(module, class_name)

        if not hasattr(class_, "from_json"):
            raise TypeError(f"class {type(obj)} does not expose a `from_json` "
                            "function")

        # Initialize the object using its `from_json` deserializer
        obj = class_.from_json(obj_data)
    return obj


# Durable Function Orchestration Trigger
class OrchestrationTriggerConverter(meta.InConverter,
                                    meta.OutConverter,
                                    binding='orchestrationTrigger',
                                    trigger=True):
    @classmethod
    def check_input_type_annotation(cls, pytype):
        return type(pytype) is type(OrchestrationContext)

    @classmethod
    def check_output_type_annotation(cls, pytype):
        # Implicit output should accept any return type
        return True

    @classmethod
    def decode(cls,
               data: meta.Datum, *,
               trigger_metadata) -> OrchestrationContext:
        return OrchestrationContext(data.value)

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        # Durable function context should be a json
        return meta.Datum(type='json', value=obj)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True


class EnitityTriggerConverter(meta.InConverter,
                              meta.OutConverter,
                              binding='entityTrigger',
                              trigger=True):
    @classmethod
    def check_input_type_annotation(cls, pytype):
        return type(pytype) is type(EntityContext)

    @classmethod
    def check_output_type_annotation(cls, pytype):
        # Implicit output should accept any return type
        return True

    @classmethod
    def decode(cls,
               data: meta.Datum, *,
               trigger_metadata) -> EntityContext:
        return EntityContext(data.value)

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        # Durable function context should be a json
        return meta.Datum(type='json', value=obj)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True


# Durable Function Activity Trigger
class ActivityTriggerConverter(meta.InConverter,
                               meta.OutConverter,
                               binding='activityTrigger',
                               trigger=True):
    @classmethod
    def check_input_type_annotation(cls, pytype):
        # Activity Trigger's arguments should accept any types
        return True

    @classmethod
    def check_output_type_annotation(cls, pytype):
        # The activity trigger should accept any JSON serializable types
        return True

    @classmethod
    def decode(cls,
               data: meta.Datum, *,
               trigger_metadata) -> typing.Any:
        data_type = data.type

        # Durable functions extension always returns a string of json
        # See durable functions library's call_activity_task docs
        if data_type in ['string', 'json']:
            try:
                callback = _deserialize_custom_object
                result = json.loads(data.value, object_hook=callback)
            except json.JSONDecodeError:
                # String failover if the content is not json serializable
                result = data.value
            except Exception:
                raise ValueError(
                    'activity trigger input must be a string or a '
                    f'valid json serializable ({data.value})')
        else:
            raise NotImplementedError(
                f'unsupported activity trigger payload type: {data_type}')

        return result

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        try:
            callback = _serialize_custom_object
            result = json.dumps(obj, default=callback)
        except TypeError:
            raise ValueError(
                f'activity trigger output must be json serializable ({obj})')

        return meta.Datum(type='json', value=result)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True


# Durable Functions Durable Client Bindings
class DurableClientConverter(meta.InConverter,
                             meta.OutConverter,
                             binding='durableClient'):
    @classmethod
    def has_implicit_output(cls) -> bool:
        return False

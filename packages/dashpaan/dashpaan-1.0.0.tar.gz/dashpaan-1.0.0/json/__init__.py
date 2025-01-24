from json import *
import json as origin

from datetime import datetime

from ..elements.base import Element
from dashpaan.elements.reverse import convert


class DashpaanJSONEncoder(origin.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Element):
            return obj.json()

        if isinstance(obj, datetime):
            # Handle datetime serialization
            return obj.isoformat()

        # Fallback to the default serialization
        return super().default(obj)


class DashpaanJSONDecoder(origin.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        # Deserialize Element
        if "kind" in obj and "version" in obj:
            return convert(obj)

        # Deserialize datetime (assuming ISO 8601 format)
        for key, value in obj.items():
            if isinstance(value, str):
                try:
                    obj[key] = datetime.fromisoformat(value)
                except ValueError:
                    pass

        return obj


JSONEncoder = DashpaanJSONEncoder
JSONDecoder = DashpaanJSONDecoder


def dumps(obj, *args, **kwargs):
    return origin.dumps(obj, cls=DashpaanJSONEncoder, *args, **kwargs)


def loads(obj, *args, **kwargs):
    return origin.loads(obj, cls=DashpaanJSONDecoder, *args, **kwargs)


__all__ = [
    'dump', 'dumps', 'load', 'loads',
    'JSONDecoder', 'JSONDecodeError', 'JSONEncoder',
]

import json

from dashpaan.elements.base import Element


class Navigation(Element):
    kind = "navigation"

    items = []

    def json(self):
        return {
            **super(Navigation, self).json(),
            "items": self.items
        }

    @classmethod
    def from_json(cls, obj):
        return Navigation(**obj)

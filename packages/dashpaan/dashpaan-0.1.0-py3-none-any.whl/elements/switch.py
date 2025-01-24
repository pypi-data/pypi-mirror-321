import json

from dashpaan.elements.base import Element


class Switch(Element):
    kind = "switch"

    type = ""
    name = ""
    label = ""

    def json(self):
        return {
            **super(Switch, self).json(),
            "type": self.type,
            "name": self.name,
            "label": self.label
        }

    @classmethod
    def from_json(cls, obj):
        return Switch(**obj)
import json

from dashpaan.elements.base import Element


class TextField(Element):
    kind = "text-field"

    name = ""
    label = ""
    required = False
    defaultValue = ""

    def json(self):
        return {
            **super(TextField, self).json(),
            "name": self.name,
            "label": self.label,
            "required": self.required,
            "defaultValue": self.defaultValue
        }

    @classmethod
    def from_json(cls, obj):
        return TextField(**obj)
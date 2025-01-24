import json

from dashpaan.elements.base import Element


class Form(Element):
    kind = "form"
    size = ""
    fields = []
    buttons = []

    def json(self):
        return {
            **super(Form, self).json(),
            "size": self.size,
            "fields": [field.json() for field in self.fields],
            "buttons": [button.json() for button in self.buttons]
        }

    @classmethod
    def from_json(cls, obj):
        return Form(**obj)

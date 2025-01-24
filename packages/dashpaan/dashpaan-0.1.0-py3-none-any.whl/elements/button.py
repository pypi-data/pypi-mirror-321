import json

from dashpaan.elements.base import Element


class Button(Element):
    kind = "button"

    title = ""
    color = ""
    action = {}

    def json(self):
        return {
            **super(Button, self).json(),
            "title": self.title,
            "color": self.color,
            "action": self.action
        }

    @classmethod
    def from_json(cls, obj):
        return Button(**obj)
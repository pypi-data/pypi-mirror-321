import json

from dashpaan.elements.base import Element


class TextAreaEditor(Element):
    kind = "text-area-editor"

    name = ""

    def json(self):
        return {
            **super(TextAreaEditor, self).json(),
            "version": self.version,
            "name": self.name
        }

    @classmethod
    def from_json(cls, obj):
        return TextAreaEditor(**obj)

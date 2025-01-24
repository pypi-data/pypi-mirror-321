import json

from dashpaan.elements.base import Element


class WYSIWYGEditor(Element):
    kind = "wysiwyg-editor"

    name = ""
    content = ""

    def json(self):
        return {
            **super(WYSIWYGEditor, self).json(),
            "name": self.name,
            "content": self.content
        }

    @classmethod
    def from_json(cls, obj):
        return WYSIWYGEditor(**obj)

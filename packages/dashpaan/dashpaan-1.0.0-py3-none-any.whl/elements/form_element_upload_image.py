import json

from dashpaan.elements.base import Element


class FormElementUploadImage(Element):
    kind = "formElementUploadImage"

    uri = ""
    title = ""
    data = [
        {
            "id": "01ff61ca-2e47-4ebe-b076-7aa9491fcbcb",
            "payload": {},
            "headers": {},
            "url": ""
        }
    ]
    variables = {
        "bookName": "The Hard Things about Hard Things",
        "categoryId": 87564521
    }

    def json(self):
        return {
            **super(FormElementUploadImage, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables
        }

    @classmethod
    def from_json(cls, obj):
        return FormElementUploadImage(**obj)

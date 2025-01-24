import json

from dashpaan.elements.base import Element


class Page(Element):
    kind = "page"

    uri = ""
    title = ""
    data = []
    variables = {}
    templates = {}
    elements = []
    navigation = "inherit"

    def json(self):
        return {
            **super(Page, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables,
            "templates": self.templates,
            "elements": [element.json() for element in self.elements],
            "navigation": self.navigation.json() if type(self.navigation) is list else self.navigation
        }

    @classmethod
    def from_json(cls, obj):
        return Page(**obj)

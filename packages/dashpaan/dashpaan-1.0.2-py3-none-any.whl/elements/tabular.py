import json

from dashpaan.elements.base import Element


class Tabular(Element):
    kind = "tabular"

    tabs = []

    def json(self):
        return {
            **super(Tabular, self).json(),
            "version": self.version,
            "tabs": self.tabs
        }

    @classmethod
    def from_json(cls, obj):
        return Tabular(**obj)

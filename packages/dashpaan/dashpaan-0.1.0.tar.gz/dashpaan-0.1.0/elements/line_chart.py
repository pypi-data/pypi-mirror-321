import json

from dashpaan.elements.base import Element


class LineChart(Element):
    kind = "chart-line"

    data = {}

    def json(self):
        return {
            **super(LineChart, self).json(),
            "version": self.version,
            "data": self.data
        }

    @classmethod
    def from_json(cls, obj):
        return LineChart(**obj)

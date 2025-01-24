import json

from dashpaan.elements.base import Element


class ChartComparison(Element):
    kind = "wave-chart"

    data = {}

    def json(self):
        return {
            **super(ChartComparison, self).json(),
            "data": self.data
        }

    @classmethod
    def from_json(cls, obj):
        return ChartComparison(**obj)
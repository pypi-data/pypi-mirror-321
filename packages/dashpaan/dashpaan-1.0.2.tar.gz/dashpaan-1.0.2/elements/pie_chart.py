import json

from dashpaan.elements.base import Element


class PieChart(Element):
    kind = "pie_chart"

    title = ""
    series = {}
    labels = []
    options = {}

    def json(self):
        return {
            **super(PieChart, self).json(),
            "title": self.title,
            "series": self.series,
            "labels": self.labels,
            "options": self.options
        }

    @classmethod
    def from_json(cls, obj):
        return PieChart(**obj)

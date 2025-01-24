import json

from dashpaan.elements.base import Element


class DonutChart(Element):
    kind = "donut-chart"

    title = ""
    series = {}
    labels = []
    options = {}

    def json(self):
        return {
            **super(DonutChart, self).json(),
            "version": self.version,
            "title": self.title,
            "series": self.series,
            "labels": self.labels,
            "options": self.options
        }

    @classmethod
    def from_json(cls, obj):
        return DonutChart(**obj)

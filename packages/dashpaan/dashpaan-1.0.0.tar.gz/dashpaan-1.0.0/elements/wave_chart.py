import json

from dashpaan.elements.base import Element


class WaveChart(Element):
    kind = "wave-chart"

    size = ""
    title = ""
    subtitle = ""
    series = {}

    def json(self):
        return {
            **super(WaveChart, self).json(),
            "size": self.size,
            "title": self.title,
            "subtitle": self.subtitle,
            "series": self.series
        }

    @classmethod
    def from_json(cls, obj):
        return WaveChart(**obj)
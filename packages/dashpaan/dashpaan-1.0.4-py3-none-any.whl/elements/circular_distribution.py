import json

from .base import Element


class CircularDistribution(Element):
    kind = "circular-distribution"

    labels = {}
    series = {}

    def json(self):
        return {
            **super(CircularDistribution, self).json(),
            "labels": self.labels,
            "series": self.series
        }

    @classmethod
    def from_json(cls, obj):
        return CircularDistribution(**obj)
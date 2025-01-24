from dashpaan.elements.base import Element


class StickyTarget(Element):
    kind = "sticky-target"

    size = ""
    color = ""
    data = {}
    more = {}

    def json(self):
        return {
            **super(StickyTarget, self).json(),
            "version": self.version,
            "size": self.size,
            "color": self.color,
            "data": self.data,
            "more": self.more
        }

    @classmethod
    def from_json(cls, obj):
        return StickyTarget(**obj)

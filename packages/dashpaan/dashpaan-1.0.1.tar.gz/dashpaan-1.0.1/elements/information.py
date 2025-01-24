from dashpaan.elements.base import Element


class Information(Element):
    kind = "information"

    title = ""
    size = ""
    information = []

    def json(self):
        return {
            **super(Information, self).json(),
            "title": self.title,
            "size": self.size,
            "information": self.information
        }

    @classmethod
    def from_json(cls, obj):
        return Information(**obj)

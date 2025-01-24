from dashpaan.elements.base import Element


class Card(Element):
    kind = "card"

    icons = []
    cover = ""
    size = ""
    title = ""
    boxes = []
    menu = {}
    description = ""

    def json(self):
        return {
            **super(Card, self).json(),
            "title": self.title,
            "size": self.size,
            "icons": self.icons,
            "boxes": self.boxes,
            "menu": self.menu,
            "description": self.description,
            "cover": self.cover
        }

    @classmethod
    def from_json(cls, obj):
        return Card(**obj)

from dashpaan.elements.base import Element


class Flex(Element):
    kind = "flex"

    class_name = ""
    mode = ""
    breakable = ""
    size = ""
    elements = []

    def json(self):
        return {
            **super(Flex, self).json(),
            "mode": self.mode,
            "breakable": self.breakable,
            "className": self.class_name,
            "size": self.size,
            "elements": [element.json() for element in self.elements]
        }

    @classmethod
    def from_json(cls, obj):
        return Flex(**obj)

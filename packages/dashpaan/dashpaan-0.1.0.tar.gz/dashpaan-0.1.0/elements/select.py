from dashpaan.elements.base import Element


class Select(Element):
    kind = "select"

    name = ""
    default = ""
    multiple = True
    label = ""
    options = []
    value = ""
    placeholder = ""

    def json(self):
        return {
            **super(Select, self).json(),
            "name": self.name,
            "default": self.default,
            "label": self.label,
            "options": self.options,
            "value": self.value,
            "placeholder": self.placeholder
        }

    @classmethod
    def from_json(cls, obj):
        return Select(**obj)

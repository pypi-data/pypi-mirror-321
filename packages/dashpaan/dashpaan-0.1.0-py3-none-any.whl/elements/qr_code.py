import json

from dashpaan.elements.base import Element


class QrCode(Element):
    kind = "qr_code"

    size = ""
    url = ""

    def json(self):
        return {
            **super(QrCode, self).json(),
            "url": self.url,
            "size": self.size,

        }

    @classmethod
    def from_json(cls, obj):
        return QrCode(**obj)

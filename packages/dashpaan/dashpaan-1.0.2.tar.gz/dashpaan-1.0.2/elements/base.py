class Element:
    kind = None
    version = "v1"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def json(self):
        return {
            "kind": self.kind,
            "version": self.version
        }

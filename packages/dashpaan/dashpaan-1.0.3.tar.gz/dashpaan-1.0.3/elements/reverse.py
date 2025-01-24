from dashpaan.elements.heading import Heading


def convert(obj):
    if "kind" in obj:
        if obj["kind"] == "heading":
            return Heading.from_json(obj)

    raise ValueError("Not Valid Element")

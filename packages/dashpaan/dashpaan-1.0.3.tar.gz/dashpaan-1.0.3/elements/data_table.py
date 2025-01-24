import json

from dashpaan.elements.base import Element


class DataTable(Element):
    kind = "data-table"

    uri = ""
    title = ""
    errors = {}
    columns = []
    rows = []

    def json(self):
        return {
            **super(DataTable, self).json(),
            "uri": self.uri,
            "title": self.title,
            "errors": self.errors,
            "columns": self.columns,
            "rows": self.rows
        }

    @classmethod
    def from_json(cls, obj):
        return DataTable(**obj)
import json
from appname.domain.model import Model


class ModelJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "id": o.id,
                "name": o.name
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

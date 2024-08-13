from appname.domain.model import Model


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Model.from_dict(i) for i in self.data]

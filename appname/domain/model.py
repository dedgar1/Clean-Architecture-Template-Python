from dataclasses import dataclass, asdict


@dataclass
class Model:
    name: str
    id: int

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return asdict(self)

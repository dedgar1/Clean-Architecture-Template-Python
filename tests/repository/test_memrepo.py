import pytest

from appname.domain.model import Model
from appname.repository.memrepo import MemRepo


def model_dicts():
    return [
        {"name": "model1", "id": 1},
        {"name": "model2", "id": 2},
        {"name": "model3", "id": 3},
        {"name": "model4", "id": 4},
    ]


def test_repository_list_without_parameters(model_dicts):
    repo = MemRepo(model_dicts)
    models = [Model.from_dict(i) for i in model_dicts]
    assert repo.list() == models

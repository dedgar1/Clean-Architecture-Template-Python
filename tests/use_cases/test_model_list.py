import pytest
from unittest import mock

from appname.domain.model import Model
from appname.use_cases.model_list import model_list_use_case


@pytest.fixture
def domain_model():
    model1 = Model('model1', 1)
    model2 = Model('model2', 2)
    model3 = Model('model3', 3)
    model4 = Model('model4', 4)
    return [model1, model2, model3, model4]


def test_model_list_without_parameters(domain_models):
    repo = mock.Mock()
    repo.list.retur_value = domain_models
    result = model_list_use_case(repo)
    repo.list.assert_called_with()
    assert result == domain_models

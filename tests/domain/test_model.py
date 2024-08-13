from appname.domain.model import Model


def test_model_from_dict():
    init_dict = {
        "name": "modelName",
        "id": 5
    }
    model = Model.from_dict(init_dict)
    assert model.id == 5
    assert model.name == "modelName"


def test_model_to_dict():
    init_dict = {
        "name": "modelName",
        "id": 5
    }
    model = Model.from_dict(init_dict)
    assert model.to_dict() == init_dict


def test_model_comparison():
    init_dict = {
        "name": "modelName",
        "id": 5
    }
    model1 = Model.from_dict(init_dict)
    model2 = Model.from_dict(init_dict)
    assert model1 == model2

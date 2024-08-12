from appname.domain.model import Model


def test_model_from_dict():
    init_dict = {
        "name": "modelName",
        "id": 5
    }
    model = Model.from_dict(init_dict)
    assert model.id == 5
    assert model.name == "modelName"

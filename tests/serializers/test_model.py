import json
from appname.domain.model import Model
from appname.serializers.model import ModelJsonEncoder


def test_serialize_domain_model():
    model = Model("modelName", 5)
    expected_json = {'id': 5, 'name': 'modelName'}
    json_model = json.dumps(model, cls=ModelJsonEncoder)
    assert json.loads(json_model) == expected_json

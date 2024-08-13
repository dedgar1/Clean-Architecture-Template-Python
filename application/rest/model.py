import json

from flask import Blueprint, Response

from appname.repository.memrepo import MemRepo
from appname.use_cases.model_list import model_list_use_case
from appname.serializers.model import ModelJsonEncoder

blueprint = Blueprint("model", __name__)

models = [
    {"name": "model1", "id": 1},
    {"name": "model2", "id": 2},
    {"name": "model3", "id": 3},
    {"name": "model4", "id": 4}
]


@blueprint.route("/models", methods=["GET"])
def model_list():
    repo = MemRepo(models)
    result = model_list_use_case(repo)
    return Response(
        json.dumps(result, cls=ModelJsonEncoder),
        mimetype="application/json",
        status=200,
    )

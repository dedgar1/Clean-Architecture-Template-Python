import json
from unittest import mock

from appname.domain.model import Model

model_dict = {'id': 1, 'name': "model1"}
models = [Model.from_dict(model_dict)]


@mock.patch("application.rest.model.model_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = models
    http_response = client.get("/models")

    print("this is resonse", http_response)
    # assert json.loads(http_response.data.decode("UTF-8")) == [model_dict]
    # mock_use_case.assert_called()
    # assert http_response.status_code == 200
    # assert http_response.mimetype == "application/json"

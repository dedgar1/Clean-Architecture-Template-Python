from appname.repository.memrepo import MemRepo
from appname.use_cases.model_list import model_list_use_case


models = [
    {"name": "model1", "id": 1},
    {"name": "model2", "id": 2},
    {"name": "model3", "id": 3},
    {"name": "model4", "id": 4},
]

repo = MemRepo(models)
result = model_list_use_case(repo)
print([model.to_dict() for model in result])

import json
import copy


class configClass:
    def __init__(self):
        self._config = {}
    def init(self, file_name:str):
         with open(file_name, 'r') as config_file:
             self._config=json.load(config_file)
    def all(self)->dict[str, str | int]:
        return copy.deepcopy(self._config)
    def get(self, name:str)->str | int:
        return copy.deepcopy(self._config[name])


import json
import copy


class configClass:
    def __init__(self):
        self._config = {}
    def init(self, file_name):
         with open(file_name, 'r') as config_file:
             self._config=json.load(config_file)
    def all(self):
        return copy.deepcopy(self._config)
    def get(self, name):
        return copy.deepcopy(self._config[name])


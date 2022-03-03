import json
import copy

__config = {};

def init(file_name):
    with open(file_name, 'r') as config_file:
         __config=json.loads(config_file.read())


def all():
    return copy.deepcopy(__config)

def get(name):
    return copy.deepcopy(__config[name])

def whiteList():
    return copy.deepcopy(__white_list)


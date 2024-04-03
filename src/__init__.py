import hnyconfig.clas as c


config = c.configClass()

def init(file_name:str):
    config.init(file_name)

def all()->dict[str, str | int]:
    return config.all()

def get(name:str)->str | int:
    return config.get(name)


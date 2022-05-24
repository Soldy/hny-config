import hnyconfig.clas as c


config = c.configClass()

def init(file_name):
    config.init(file_name)

def all():
    return config.all()

def get(name):
    return config.get(name)


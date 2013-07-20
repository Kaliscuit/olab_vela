import uuid

def new(type=''):
    return type + '_' + uuid.uuid1()
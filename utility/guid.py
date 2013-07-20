import uuid

def new(type=''):
    return type + '_' + str(uuid.uuid1())
#! /usr/bin/env python
import datetime

class Content():

    '''
    Content Model
    Base properties and funcctions
    '''

    def __init__(self,db,id):
        self._db = db
        content = self.get_item(id)

    @property
    def db(self):
        return self._db

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def content_time(self):
        return self._content_time    

    @property
    def data(self):
        return self._data    


    @property
    def create_time(self):
        return self._create_time
        
    @property
    def update_time(self):
        return self._update_time

    def get_one(self,id):
        self._id = id
        content = self.db.content.find_one({'id' : self.id})
        if content:
            self._type = content['type']
            self._content_time = content['content_time']
            self._data = content['data']
            self._contents = content['contents']
            self._create_time = content['create_time']
            self._update_time = content['update_time']
        else:
            self._content_time = ''
            self._creator = ''
            self._members = []
            self._contents = []
            self._create_time = datetime.datetime.utcnow()
            self._update_time = datetime.datetime.utcnow()
            
    def get_properties(self):
        properties = {
            'id': self.id,
            'content_time': self.content_time,
            'creator': self.creator,
            'members': self.members,
            'contents': self.contents,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
        return properties

    def save(self):
        properties = self.get_properties()
        properties['update_time'] = datetime.datetime.utcnow()
        self.db.content.update({'id': self.id}, properties, upsert=True)

    

            


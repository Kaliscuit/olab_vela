#! /usr/bin/env python
import datetime


class Vela():
    '''
    Vela Model
    Base properties and functions
    '''

    def __init__(self, db, id):
        self._db = db
        vela = self.get_item(id)
        
    @property
    def id(self):
        return self._id

    @property
    def db(self):
        return self._db

    @property
    def owner(self):
        return self._owner

    @property
    def members(self):
        return self._members

    @property
    def routes(self):
        return self._routes

    @property
    def create_time(self):
        return self._create_time

    @property
    def update_time(self):
        return self._update_time

    def get_item(self, id):
        self._id = id
        vela = self.db.vela.find_one({'id': self.id})
        if vela:
            self._owner = vela['owner']
            self._members = vela['members']
            self._routes = vela['routes']
            self._create_time = vela['create_time']
            self._update_time = vela['update_time']
        else:
            self._owner = ''
            self._members = []
            self._routes = []
            self._create_time = datetime.datetime.utcnow()
            self._update_time = datetime.datetime.utcnow()

    def get_properties(self):
        properties = {
            'id': self.id
            'owner': self.owner,
            'members': self.members,
            'routes': self.routes,
            'create_time': self.create_time,
            'update_time': self.update_time,
        }
        return properties

    def save(self):
        properties = self.get_properties()
        properties['update_time'] = datetime.datetime.utcnow()
        self.db.vela.update({'id': self.id}, properties, upsert=True)
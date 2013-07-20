#! /usr/bin/env python
import datetime


class User():
    '''
    User Model
    Base properties and functions
    '''

    def __init__(self, db, id):
        self._db = db
        user = self.get_item(id)
        
    @property
    def id(self):
        return self._id
        
    @property
    def db(self):
        return self._db

    @property
    def nickname(self):
        return self._nickname

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def register_time(self):
        return self._register_time

    @property
    def update_time(self):
        return self._update_time

    def get_item(self, id):
        self._id = id
        user = self.db.user.find_one({'id': self.id})
        if user:
            self._email = user['email']
            self._nickname = user['nickname']
            self._password = user['password']
            self._register_time = user['register_time']
            self._update_time = user['update_time']
        else:
            self._email = ''
            self._nickname = ''
            self._password = ''
            self._register_time = datetime.datetime.utcnow()
            self._update_time = datetime.datetime.utcnow()

    def get_properties(self):
        properties = {
            'id': self.id,
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password,
            'register_time': self.register_time,
            'update_time': self.update_time
        }
        return properties

    def save(self):
        properties = self.get_properties()
        properties['update_time'] = datetime.datetime.utcnow()
        self.db.user.update({'id': self.id}, properties, upsert=True)
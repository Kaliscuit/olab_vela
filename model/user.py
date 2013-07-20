#! /usr/bin/env python
import datetime


class User():
    '''
    User Model
    Base properties and functions
    '''

    def __init__(self, db, user_email):
        self._db = db
        user = self.get_user(user_email)

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

    def get_user(self, user_email):
        self._email = user_email
        user = self.db.user.find_one({'email': self.email})
        if user:
            self._nickname = user['nickname']
            self._password = user['password']
            self._register_time = user['register_time']
            self._update_time = user['update_time']
        else:
            self._nickname = ''
            self._password = ''
            self._register_time = ''
            self._update_time = ''

    def get_properties(self):
        properties = {
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password,
            'register_time': datetime.datetime.utcnow(),
            'update_time': datetime.datetime.utcnow()
        }
        return properties

    def save(self):
        properties = self.get_properties()
        self.db.user.update({'email': self.email}, properties, upsert=True)
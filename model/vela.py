# /usr/bin/env python
import datetime


class Vela():

    '''
    Vela Model
    Base properties and functions
    '''

    def __init__(self, db):
        self._db = db
        self._owner = ''
        self._members = ''
        self._routes = ''
        self._create_time = ''

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

    def create(self):
        properties = {
                'owner':self._owner,
                'members':self._members,
                'routes':self._routes,
                'create_time':datetime.datetime.utnow()
                }
        db.vela.insert(properties)

    def add_snap_to_route(self, snap_id):
        self._routes.append(snap_id)
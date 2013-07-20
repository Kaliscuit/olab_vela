#! /usr/bin/env python
import datetime

class Snap():

    '''
    Snap Model
    Base properties and funcctions
    '''

    def __init__(self,db,id):
        self._db = db
        snap = self.get_snap(id)

    @property
    def db(self):
        return self._db

    @property
    def snap_time(self):
        return self._snap_time

    @property
    def creator(self):
        return self._creator

    @property
    def members(self):
        return self._members

    @property
    def members(self):
        return self._contents

    def get_snap(self,id):
        self._id = id
        snap = self.db.snap.find_one({'id' : self.id})
        if id:
            self._snap_time = snap['snap_time']
            self._creator = snap['creator']
            self._members = snap['members']
            self._contents = snap['continue']
        else:
            self._snap_time = ''
            self._creator = ''
            self._members = ''
            self._conetents = ''

            


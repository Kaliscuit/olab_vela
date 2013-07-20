#! /usr/bin/env python
import datetime

class Snap():

    '''
    Snap Model
    Base properties and funcctions
    '''

    def __init__(self,db,id):
     self._db = db
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

    def get_snap(self):

    


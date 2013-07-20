#! /usr/bin/env python

import pymongo


client = pymongo.MongoClient("localhost", 20517)
db = client.vela

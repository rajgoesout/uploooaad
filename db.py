from pymongo import MongoClient

from .settings import MONGO_URI

client = MongoClient(MONGO_URI)
dbs = client.uploooaad

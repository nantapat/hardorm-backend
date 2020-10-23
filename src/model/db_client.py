from pymongo import MongoClient
class DBClient():
    def __init__(self):
        self.client = MongoClient("hardorm-db",27017,username='nannapas',password='1234')
        self.db = self.client["hardorm-db"]
    def get_user_collection(self):
        return self.db["user"]
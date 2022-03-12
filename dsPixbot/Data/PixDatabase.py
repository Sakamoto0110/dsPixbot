import pymongo
from pymongo import MongoClient

class PixDatabase:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        return
    def GetDB(self,name):
        return self.client[name]
    def Update(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        
DB_CLIENT ={}
DB_NAME = "PixMemory"
DB = {}
def Init():
    DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")     

def SetActiveDB(db_name):
    if(DB_NAME is DB_CLIENT.values()):
        DB = DB_CLIENT[db_name]
    else:
        DB_CLIENT[db_name] = {}
        DB = DB_CLIENT[db_name]
    return DB

# Tables
TB_DUMMYBLOB = "DummyBlob"
TB_PESSOAS = "Pessoas"





def GetTable(tb_name):
    if(tb_name in DB.values()):
        return DB[tb_name]
    DB[tb_name] = {}
    return DB[tb_name]
    

def AddData(tb_name, obj):
    DB[tb_name].insert_one(obj)
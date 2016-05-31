import pymongo
import random
import datetime

from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.workshop

types = db.Types

ty = {"int" : 42, "float" : 42.42, "string" : "string","boolen" : True, "array" : ["rouge", "bleu", "verre"], "document" : {"type" : "document", "name" : "classified"}, "date" : datetime.datetime.utcnow()}

types.insert_one(ty)




i = 0
random.seed(42)
users = db.Users

types = {1 : "payant", 2 : "gratuit", 3 : "freemium"}

while i < 2000000:

    if (i % 3 == 0):
        address = {"zip" : 75001, "city" : "Paris", "street" : "blabla"}
        tags = ["vert","bleu"]
    else:
        address = None

    if (i % 7 == 0):
        tags = ["jaune", "rouge"]

    user = {"tags":tags, "name": "Name" + str(i), "type": types[random.randint(1, 3)], "xp": random.randint(0, 1000), "address": address, "birthday" :datetime.datetime.utcnow()}

    if (i % 5 == 0):
        del user["birthday"]


    user_id = users.insert_one(user).inserted_id
    i = i + 1



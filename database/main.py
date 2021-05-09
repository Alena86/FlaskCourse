from pymongo import MongoClient

mongoServer = "localhost"
mongoPort = 27017

client = MongoClient(mongoServer, mongoPort)

db = client["microlog"]
# Create an entry in the database
# db.entries.insert_one({"db":"MongoDB", "type": "NoSQL", "dbName": "microblog", "collection": "entries"})

entries = db.entries.find()
for entry in entries: 
    print(entry)
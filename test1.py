import pymongo
client = pymongo.MongoClient("mongodb+srv://Ritesh1212:Indigo5444@cluster0.hzs0x.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



d= {
    'name': 'Ritesh',
    'email_id': 'ritesh@gmail.com',
    'surname': 'Kumar'
}

db1 = client['mongotest']
coll = db['test1']
coll.insert_one(d)

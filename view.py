from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["BJPSB"]
collection = db["blockwords"]
for i in collection.find({"name": "买卖黑卡"}):
	print(i)
# print(collection.count_documents({}))
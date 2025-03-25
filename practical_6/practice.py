import pymongo
import time

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.2")

db = client["testdataset"]

collection = db["users"]

collection.insert_many([
    {
        "name": "alex",
        "age": 21
    },
    {
        "name": "john",
        "age": 22
    },
    {
        "name": "ela",
        "age": 23
    }
])

#Query without indexing
print("Quering data without indexing")
start_time = time.time()
result = collection.find_one({ "age" : 23 })
print("result", result)
end_time = time.time()
print(f"Query time without index: {end_time - start_time} seconds")

collection.create_index([("age", 1)])

print("Quering data with indexing")
start_time = time.time()
result = collection.find_one({ "age" : 23 })
print("result", result)
end_time = time.time()
print(f"Query time with index: {end_time - start_time} seconds")

indexes = collection.index_information()

print("indexes", indexes)
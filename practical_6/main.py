from pymongo import MongoClient
import time

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.4.2")

db = client["testdataset"]

collection = db["users"]

collection.insert_many([
    { "name": "Alice", "age": 25, "city": "New York" },
  { "name": "Bob", "age": 30, "city": "Los Angeles" },
  { "name": "Charlie", "age": 35, "city": "Chicago" },
])

#Query without index
start_time = time.time()
result = collection.find({ "age" : 25 })
end_time = time.time()

print(f"Query time without index: {end_time - start_time} seconds")

collection.create_index([("age" , 1)])

print("Index created on 'age' field")

start_time = time.time()
result = collection.find({ "age" : 25 })
list(result)
end_time = time.time()

print(f"Query time with index: {end_time - start_time} seconds")

#View indexes
indexes = collection.index_information()

print("Indexes:", indexes)
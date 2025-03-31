from pymongo import MongoClient
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
DB_url=config['MONGODB']['DB_URL']


client = MongoClient(DB_url)
db = client['database']
collection = db['movie']

"""

# Retrieve and display the latest 10 comments
documents = db['comment'].find({'name':'Forrest Gump'},{"comment": 1,"datetime":1,"_id": 0}).sort("datetime", -1).limit(10)  # Sort by datetime descending, limit to 10
latest_comments=list(document['comment'] for document in documents)
print("Latest Comments:",latest_comments)
#for comment in latest_comments:
#    print(f"Movie: {comment['name']}, Comment: {comment['comment']}, DateTime: {comment['datetime']}")


# Retrieve and print all documents

query={}
documents = collection.find(query)

for document in documents:
    print(document)
    

# Use distinct to get unique movie names
unique_movie_names = collection.distinct("name")
# Print the list of unique movie names
print("Unique Movie Names:")
for name in unique_movie_names:
    print(name)



"""
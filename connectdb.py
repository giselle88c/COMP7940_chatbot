from pymongo import MongoClient
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
DB_url=config['MONGODB']['DB_URL']


client = MongoClient(DB_url)
db = client['database']
collection = db['sensors']

temperature=27
humidity =50

# Create a record variable to store the sensor data
record = {
   "sensor_id": 1,
   "temp": temperature,
   "humi": humidity,
   "date": datetime.datetime.now(),
}

# Insert the record
#collection.insert_one(record)


# Retrieve and print all documents
query = {"temp": 27}
documents = collection.find(query)

for document in documents:
    print(document)
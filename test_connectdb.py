from pymongo import MongoClient
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
DB_url=config['MONGODB']['DB_URL']


client = MongoClient(DB_url)
db = client['database']
collection = db['movie']


# Create a record variable to store the sensor data
records = [
    {
        "movie_id": 1,
        "name": 'Inception',
        "description": 'A mind-bending thriller by Christopher Nolan.'
    },
    {
        "movie_id": 2,
        "name": 'The Dark Knight',
        "description": 'A thrilling tale of Batman and the Joker directed by Christopher Nolan.'
    },
    {
        "movie_id": 3,
        "name": 'The Shawshank Redemption',
        "description": 'An inspiring drama about hope and friendship.'
    },
    {
        "movie_id": 4,
        "name": 'Pulp Fiction',
        "description": 'A stylistic thriller that intertwines various storylines.'
    },
    {
        "movie_id": 5,
        "name": 'The Godfather',
        "description": 'An epic tale of family and power in the criminal underworld.'
    },
    {
        "movie_id": 6,
        "name": 'Fight Club',
        "description": 'A tale of identity and consumerism narrated by an unnamed protagonist.'
    },
    {
        "movie_id": 7,
        "name": 'The Matrix',
        "description": 'A science fiction classic that explores reality and illusion.'
    },
    {
        "movie_id": 8,
        "name": 'Forrest Gump',
        "description": 'The life journey of a simple man with a big heart.'
    },
    {
        "movie_id": 9,
        "name": 'Interstellar',
        "description": 'A visually stunning journey through space and time.'
    },
    {
        "movie_id": 10,
        "name": 'Gladiator',
        "description": 'A Roman general seeks revenge against a corrupt emperor.'
    },
        # Hong Kong Movies
    {
        "movie_id": 11,
        "name": 'Infernal Affairs',
        "description": 'A thrilling tale of undercover police and gangsters in Hong Kong.'
    },
    {
        "movie_id": 12,
        "name": 'Chungking Express',
        "description": 'A romantic drama interweaving the lives of two police officers.'
    },
    {
        "movie_id": 13,
        "name": 'The Grandmaster',
        "description": 'A martial arts biopic of the legendary Wing Chun master Ip Man.'
    },
    {
        "movie_id": 14,
        "name": 'Hero',
        "description": 'An epic war film showcasing the beauty of martial arts and heroism.'
    },
    {
        "movie_id": 15,
        "name": 'Kung Fu Hustle',
        "description": 'A comedic martial arts film that combines humor and action.'
    },
    {
        "movie_id": 16,
        "name": 'Crouching Tiger, Hidden Dragon',
        "description": 'A visually stunning film that tells a tale of love and honor through martial arts.'
    },
    {
        "movie_id": 17,
        "name": 'The Killer',
        "description": 'A story of an assassins conflict between duty and love.'
    },
    {
        "movie_id": 18,
        "name": 'Police Story',
        "description": 'A classic action-comedy thriller featuring Jackie Chan signature stunts.'
    },
    {
        "movie_id": 19,
        "name": 'A Better Tomorrow',
        "description": 'A film about brotherhood and loyalty that reshaped the Hong Kong action genre.'
    },
    {
        "movie_id": 20,
        "name": 'The Wong Fei Hung Series',
        "description": 'A series of films portraying the legendary martial artist Wong Fei Hung.'
    }
]

# Insert the movie records into the MongoDB collection
#collection.insert_many(records)


   #

"""
# Insert the record
comment={"name":'The Matrix','comment':'Excellent!',"datetime": datetime.datetime.now()}
#db['comment'].insert_one(comment)


# Function to retrieve the latest 10 comments
def get_latest_comments():
    latest_comments = db['comment'].find().sort("datetime", -1).limit(10)  # Sort by datetime descending, limit to 10
    return latest_comments

# Retrieve and display the latest 10 comments
documents = db['comment'].find({'name':'Forrest Gump'},{"comment": 1,"datetime":1,"_id": 0}).sort("datetime", -1).limit(10)  # Sort by datetime descending, limit to 10
latest_comments=list(document['comment'] for document in documents)
print("Latest Comments:",latest_comments)
#for comment in latest_comments:
#    print(f"Movie: {comment['name']}, Comment: {comment['comment']}, DateTime: {comment['datetime']}")



"""

# Retrieve and print all documents""

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
documents = collection.find({'name':'The Matrix'}, {"name": 1, "description": 1, "_id": 0})  # Excludes the "_id", includes "name" and "description"
#movies = [{ "name": document['name'], "description": document['description'] } for document in documents]
print(documents[0]['name'])"

"""


import random

# List of movies
movies = [
    "Fight Club",
    "Forrest Gump",
    "Gladiator",
    "Inception",
    "Interstellar",
    "Pulp Fiction",
    "The Dark Knight",
    "The Godfather",
    "The Matrix",
    "The Shawshank Redemption"
]
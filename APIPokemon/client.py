from pymongo import MongoClient

client = MongoClient().local

db = client["pokedb"]

db_pokemon = db["pokemon"]

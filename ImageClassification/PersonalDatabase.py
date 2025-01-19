from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
CONNECTION_STRING = f"mongodb+srv://stevenzdragons:{PASSWORD}@enelingo.qn39p.mongodb.net/?retryWrites=true&w=majority&appName=Enelingo"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

users_collection = db["users"]


def register_user(username, firstname, lastname, email, password, cityofresidence):
    user_info = {
        "user":username,
        "first_name":firstname,
        "last_name":lastname,
        "email":email,
        "password":password,
        "city_of_residence":cityofresidence
    }
    users_collection.insert_one(user_info)



appliance_collection = db["appliances"]

def register_appliances(appliances, user):
    appliances_info = {
        "appliances":appliances,
        "user":user
    }
    appliance_collection.insert_one(appliances_info)


#register_user("binky", "Nathan", "A", "binkybarnes@gmail.com", "iambinky", "Atlanta")


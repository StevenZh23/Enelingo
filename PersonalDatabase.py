from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

#API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
CONNECTION_STRING = f"mongodb+srv://stevenzdragons:{PASSWORD}@enelingo.qn39p.mongodb.net/?retryWrites=true&w=majority&appName=Enelingo"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

users_collection = db["users"]


def register_user(username, firstname, lastname, email, password, cityofresidence, currentcost, costwatt, budget, spent):
    user_info = {
        "user":username,
        "first_name":firstname,
        "last_name":lastname,
        "email":email,
        "password":password,
        "city_of_residence":cityofresidence,
        "current_cost_per_minute":currentcost,
        "cost_per_watt_minute":costwatt,
        "budget":budget,
        "spent":spent,
        "streak": 0
    }
    users_collection.insert_one(user_info)



appliance_collection = db["appliances"]

def register_appliances(appliancename, appliancetype, wattage, user, onoff):
    appliances_info = {
        "appliance_name":appliancename,
        "appliance_type":appliancetype,
        "wattage":wattage,
        "user":user,
        "onoff":onoff
    }
    appliance_collection.insert_one(appliances_info)


location_collection = db["locations"]

def register_location(locationname, costperwatt):
    location_info = {
        "city_name": locationname,
        "cost_per_watt_($/wattminute)":costperwatt
    }
    location_collection.insert_one(location_info)


def turn_on_off(user, appliancename):
    x = appliance_collection.find({'user': user, 'appliance_name': appliancename})
    y = users_collection.find({"user":user})
    x = x[0]
    y = y[0]
    to_update = y["current_cost_per_minute"]

    if x["onoff"] == "on":
        appliance_collection.update_one(
            {"user": user, "appliance_name":appliancename}, # Query to match
            {"$set": {"onoff": "off"}}             # Update operation
        )

        users_collection.update_one(
            {"user": user},
            {"$set": {"current_cost_per_minute": to_update - x['wattage'] * y["cost_per_watt_minute"]}}
        )

    elif x["onoff"] == "off":
        appliance_collection.update_one(
            {"user": user, "appliance_name":appliancename}, # Query to match
            {"$set": {"onoff": "on"}})             # Update operation
        users_collection.update_one(
            {"user": user},
            {"$set": {"current_cost_per_minute": to_update + x['wattage'] * y["cost_per_watt_minute"]}}
        )

    else:
        print("You broke it")


def spend_energy(user):
    x = users_collection.find({"user":user})
    x = x[0]
    users_collection.update_one(
        {"user":user},
        {"$set": {"spent": x["spent"] + x["current_cost_per_minute"]}}
    )

def change_budget(user, budget):
    users_collection.update_one(
        {"user":user},
        {"$set": {"budget":budget}}
    )

def reset_spent(user):
    x = users_collection.find({"user":user})
    x = x[0]["streak"]
    users_collection.update_one(
        {"user":user},
        {"$set": {"spent":0, "streak":x+1} }
    )

#register_location("Atlanta", 0.17 / 60000)
#register_appliances("Ultratoaster", "toaster", 25000, "binky", "off")
#register_user("binky", "Nathan", "A", "binkybarnes@gmail.com", "iambinky", "Atlanta", 0, .17/60000, 200, 0)

#change_budget("binky", 300)
turn_on_off("binky", "Ultratoaster")
spend_energy("binky")

reset_spent("binky")
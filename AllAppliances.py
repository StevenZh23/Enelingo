from PersonalDatabase import get_database

db = get_database()

all_appliance_collection = db["all_appliances"]

def register_appliance_toList(appliancename, appliancetype, wattage):
    appliances_info = {
        "appliance_name":appliancename,
        "appliance_type":appliancetype,
        "wattage":wattage,
    }
    all_appliance_collection.insert_one(appliances_info)


register_appliance_toList("Ultratoaster", "Toaster", 25000)
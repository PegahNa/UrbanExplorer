import json
import os

def get_data_for_city(city):
    location_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "locations.json")
    with open(location_file, "r") as file:
        locations_data = json.load(file)

    city_data = locations_data.get(city.lower())  # Convert city to lowercase to match the JSON keys
    return city_data if city_data else []

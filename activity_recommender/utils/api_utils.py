import json


def get_data_for_city(city):
    with open("/mnt/data/locations.json", "r") as file:
        locations_data = json.load(file)

    city_data = locations_data.get(city.lower())  # Convert city to lowercase to match the JSON keys
    return city_data if city_data else []

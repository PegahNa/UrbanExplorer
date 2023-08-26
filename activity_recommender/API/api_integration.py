import requests

API_KEY = "AhcE7S6Z6D68upadbXn1dZ_lwIjESjIbpBLSKRoyC5ZtpEFQ_oU9Y2GoOwodUgq0"
BASE_URL = "http://dev.virtualearth.net/REST/v1/Locations"


def get_location_info(query):
    params = {
        "q": query,
        "key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and data.get("resourceSets"):
        resources = data["resourceSets"][0]["resources"]
        if resources:
            location = resources[0]
            coordinates = location.get("point", {}).get("coordinates")
            latitude, longitude = coordinates if coordinates else (None, None)
            address = location.get("address", {})
            formatted_address = address.get("formattedAddress", "Unknown")
            return formatted_address, latitude, longitude
    return "Location not found", None, None


def get_url(location_to_search):
    #2user_input = input("Enter a destination: ")
    location, latitude, longitude = get_location_info(location_to_search)

    if latitude is not None and longitude is not None:
        bing_maps_url = f"http://www.bing.com/maps?cp={latitude}~{longitude}"
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        return f"Location: {location}\nBing Maps URL: {bing_maps_url}\nGoogle Maps URL: {google_maps_url}"
    else:
        return location


if __name__ == "__main__":
    result = get_url()


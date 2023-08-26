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
            address = location.get("address", {})
            formatted_address = address.get("formattedAddress", "Unknown")
            return formatted_address
    return "Location not found"

def main():
    user_input = input("Enter a destination: ")
    location = get_location_info(user_input)
    print(f"Location: {location}")


if __name__ == "__main__":
    main()

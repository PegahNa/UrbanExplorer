import requests

search_query = "Eiffel Tower"
bingApiKey = "AhcE7S6Z6D68upadbXn1dZ_lwIjESjIbpBLSKRoyC5ZtpEFQ_oU9Y2GoOwodUgq0"
base_url = "http://dev.virtualearth.net/REST/v1/Locations"

# Step 1: Search for the place using the text query
search_url = f"{base_url}?q={search_query}&key={bingApiKey}"
search_response = requests.get(search_url)
search_data = search_response.json()

if "resourceSets" in search_data and len(search_data["resourceSets"]) > 0:
    resources = search_data["resourceSets"][0]["resources"]

    if len(resources) > 0:
        place = resources[0]  # Assuming the first result is the desired place
        address = place["address"]["formattedAddress"]
        coordinates = place["point"]["coordinates"]  # Latitude and Longitude

        # Step 2: Use the coordinates to get more details about the place
        reverse_url = f"{base_url}/{coordinates[0]},{coordinates[1]}?o=json&key={bingApiKey}"
        reverse_response = requests.get(reverse_url)
        reverse_data = reverse_response.json()

        if "resourceSets" in reverse_data and len(reverse_data["resourceSets"]) > 0:
            resource = reverse_data["resourceSets"][0]["resources"][0]
            business_info = resource["businesses"][0] if "businesses" in resource else None

            if business_info:
                opening_hours = business_info.get("businessInfo", {}).get("HoursOfOperation", None)

                if opening_hours:
                    opening_info = ""
                    for day, hours in opening_hours.items():
                        opening_info += f"{day.capitalize()}: {hours[0]['OpenTime']}-{hours[0]['CloseTime']}; "

                    opening_info = opening_info[:-2]  # Remove the trailing "; "
                    print(f"Address: {address}")
                    print(f"Opening Hours: {opening_info}")
                else:
                    print("Opening hours not available.")
            else:
                print("Business details not found in response.")
        else:
            print("Reverse geocoding details not found in response.")
    else:
        print("No results found for the search query.")
else:
    print("Resource sets not found in response.")


import json

def load_locations_data():
    with open('data/locations.json') as json_file:
        data = json.load(json_file)
    return data

def main():
    locations_data = load_locations_data()

    for location, activities in locations_data.items():
        print(f"{location.capitalize()} activities:")
        for activity in activities:
            print("Activity:", activity['activity'])
            print("Price:", activity['price'])
            print("Rating:", activity['rating'])
            print("Wheelchair Accessible Entrance:", activity['wheelchair_accessible_entrance'])
            print("Hearing Accessibility:", activity['hearing_accessibility'])
            print("Visual Accessibility:", activity['visual_accessibility'])
            print("Opening Hours:", activity['opening_hours'])
            print("Current Opening Hours:", activity['current_opening_hours'])
            print()  # Print a newline for better readability

if __name__ == "__main__":
    main()
    
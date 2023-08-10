import json

# This is just to test my function, it'll be deleted later
with open('C:/Users/Fabiana/Downloads/CFG degree/Group-1-activity-recommender/data/locations.json') as json_file:
    fake_data = json.load(json_file)


    class Filter:
        def __init__(self, city):
            self.city = city

        def print_city(self):
            print(self.city)

        def filter_by_price(self, target_price):
            result = [item for item in self.city if item["price"] in target_price]
            pretty_result = json.dumps(result, indent=4)
            print(pretty_result)

        def filter_by_rating(self, target_rating):
            result = [item for item in self.city if item["rating"] in target_rating]
            pretty_result = json.dumps(result, indent=4)
            print(pretty_result)


    madrid = Filter(fake_data["spain"])
    madrid.print_city()
    madrid.filter_by_price(range(2,10))
    madrid.filter_by_price(range(12, 20))
    madrid.filter_by_price(range(20, 50))

    four_stars = [4.0 + (x * 0.1)
             for x in range(0, 10)]

    madrid.filter_by_rating(four_stars)
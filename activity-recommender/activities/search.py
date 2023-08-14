import json

five_stars = [5.0]
# Create a range of decimal numbers from 4.0 to 4.9
four_stars = [4.0 + (x * 0.1)
             for x in range(0, 10)]
three_stars = [3.0 + (x * 0.1)
             for x in range(0, 10)]
two_stars = [2.0 + (x * 0.1)
             for x in range(0, 10)]
one_stars = [1.0 + (x * 0.1)
             for x in range(0, 10)]
zero_stars = [0.0 + (x * 0.1)
             for x in range(0, 10)]


class Filter:
    def __init__(self, city):
        self.city = city

    def filter_by_price(self, target_price):
        result = [item for item in self.city if item["price"] in target_price]
        pretty_result = json.dumps(result, indent=4)
        return pretty_result

    def filter_by_rating(self, target_rating):
        result = [item for item in self.city if item["rating"] in target_rating]
        pretty_result = json.dumps(result, indent=4)
        return pretty_result

    def filter_by_wheelchair_accessible_entrance(self):
        result = [item for item in self.city if item["wheelchair_accessible_entrance"] == True]
        pretty_result = json.dumps(result, indent=4)
        print("wheelchair_accessible_entrance")
        return pretty_result

    def filter_by_hearing_accessibility(self):
        result = [item for item in self.city if item["hearing_accessibility"] == True]
        pretty_result = json.dumps(result, indent=4)
        print("hearing_accessibility")
        return pretty_result

    def filter_by_visual_accessibility(self):
        result = [item for item in self.city if item["visual_accessibility"] == True]
        pretty_result = json.dumps(result, indent=4)
        print("visual_accessibility")
        return pretty_result

    def filter_by_current_opening_hours(self):
        result = [item for item in self.city if item["current_opening_hours"] == "open_now"]
        pretty_result = json.dumps(result, indent=4)
        print("current_opening_hours")
        return pretty_result
import json
import datetime


# To evaluate how many stars is the rating of an activity
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


# Custom exception to raise an error if user asks for a rating higher than 5 stars
class RatingHigherThan5Stars(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
        print("self.value ", self.value)

    # __str__ is to print() the value
    def __str__(self):
        return (f"The rating {self.value} is not in the range of 1-5 stars")

# Class that will filter all the key-values options on our JSON file
class Filter:
    # Specify to which city user is travelling
    def __init__(self, city):
        self.city = city

    def filter_by_price(self, target_price):
        result = [item for item in self.city if item["price"] in target_price]
        pretty_result = json.dumps(result, indent=4)
        return pretty_result

    def filter_by_rating(self, target_rating):
        try:
            if target_rating[0] not in [0, 1, 2, 3, 4, 5.0]:
                raise RatingHigherThan5Stars(target_rating)
            else:
                result = [item for item in self.city if item["rating"] in target_rating]
                pretty_result = json.dumps(result, indent=4)
                return pretty_result
        except RatingHigherThan5Stars as err:
            return ("The rating requested is not in the range of 1-5 stars", err.value)


    def filter_by_wheelchair_accessible_entrance(self):
        result = [item for item in self.city if item["wheelchair_accessible_entrance"] is True]
        pretty_result = json.dumps(result, indent=4)
        print("wheelchair_accessible_entrance")
        return pretty_result

    def filter_by_hearing_accessibility(self):
        result = [item for item in self.city if item["hearing_accessibility"] is True]
        pretty_result = json.dumps(result, indent=4)
        print("hearing_accessibility")
        return pretty_result

    def filter_by_visual_accessibility(self):
        result = [item for item in self.city if item["visual_accessibility"] is True]
        pretty_result = json.dumps(result, indent=4)
        print("visual_accessibility")
        return pretty_result

    def filter_by_current_opening_hours(self):
        result = [item for item in self.city if item["current_opening_hours"] == "open_now"]
        pretty_result = json.dumps(result, indent=4)
        print("current_opening_hours")
        return pretty_result

    # Filter by the date and time inputted by user (if they're planning on going in the future)
    # It checks what day is for that date (i.e. Monday, Friday, etc.) and what activities will be open on that day and at that time
    def filter_by_opening_hours(self, target_date, target_time):
        date_format = "%d/%m/%Y"
        date_time = "%H:%M"

        # It gets the target day in format "Monday" and the target time in format "12:05"
        day_target = datetime.datetime.strptime(target_date, date_format).strftime("%A")
        time_target = datetime.datetime.strptime(target_time, date_time).strftime("%H:%M")

        open_activities = []

        # For activities open 24hs and activities that much in time and day, append to open_activities
        for item in self.city:
            if item["opening_hours"]["everyday"] == "24hs":
                open_activities.append(item)
            elif item["opening_hours"]["specific_times"] is not None:
                for opening in item["opening_hours"]["specific_times"]:
                     if opening["day"] == day_target and opening["open"] <= time_target <= opening["close"]:
                        open_activities.append(item)
                        break

        pretty_result = json.dumps(open_activities, indent=4)
        return pretty_result

    # Check what activities are open at the moment (current date and time)
    def filter_by_current_opening_hours(self):
        current_day = datetime.datetime.now().strftime("%A")
        current_time = datetime.datetime.now().strftime("%H:%M")

        open_activities = []

        for item in self.city:
            if item["opening_hours"]["everyday"] == "24hs":
                open_activities.append(item)
            elif item["opening_hours"]["specific_times"] is not None:
                for opening in item["opening_hours"]["specific_times"]:
                     if opening["day"] == current_day and opening["open"] <= current_time <= opening["close"]:
                        open_activities.append(item)
                        break

        pretty_result = json.dumps(open_activities, indent=4)
        return pretty_result



# paris_data = [
#             {
#               "activity": "Eiffel Tower",
#               "price": 16,
#               "rating": 4.7,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": True,
#               "visual_accessibility": True,
#               "opening_hours": "daily 9:00-00:45",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Louvre Museum",
#               "price": 15,
#               "rating": 4.8,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": True,
#               "visual_accessibility": True,
#               "opening_hours": "mon, thu, sat, sun 9:00-18:00, wed, fri 9:00-21:45",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Notre-Dame Cathedral",
#               "price": 0,
#               "rating": 4.6,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": False,
#               "visual_accessibility": False,
#               "opening_hours": "daily 8:00-18:45",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Montmartre",
#               "price": 0,
#               "rating": 4.5,
#               "wheelchair_accessible_entrance": False,
#               "hearing_accessibility": False,
#               "visual_accessibility": False,
#               "opening_hours": "24hs",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Seine River Cruise",
#               "price": 12,
#               "rating": 4.7,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": True,
#               "visual_accessibility": True,
#               "opening_hours": "daily 9:00-23:00",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Versailles Palace",
#               "price": 20,
#               "rating": 4.6,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": True,
#               "visual_accessibility": True,
#               "opening_hours": "tue-sun 9:00-18:30",
#               "current_opening_hours": "open_now"
#             },
#             {
#               "activity": "Centre Pompidou",
#               "price": 14,
#               "rating": 4.5,
#               "wheelchair_accessible_entrance": True,
#               "hearing_accessibility": True,
#               "visual_accessibility": True,
#               "opening_hours": "wed-mon 11:00-21:00",
#               "current_opening_hours": "open_now"
#             }]
#
# # testing_paris = Filter(paris_data)
#
# # print(testing_paris.filter_by_rating("n"))
# #print(testing_paris.filter_by_rating(four_stars))
# #print(testing_paris.filter_by_rating([6.0]))
#
# # # Testing the filters
#
# fake_data = []
#
# # This is just to test my function, it'll be deleted later
# with open('C:/Users/Fabiana/Downloads/CFG degree/Group-1-activity-recommender/data/locations.json') as json_file:
#     fake_data = json.load(json_file)
#
# # print("Madrid")
# madrid = Filter(fake_data["madrid"])
# paris = Filter(fake_data["paris"])
# new_york = Filter(fake_data["new york"])
# print("Madrid. filter_by_opening_hours")
# print(madrid.filter_by_opening_hours("12/05/2023", "23:55"))
# print("Madrid. filter_by_current_opening_hours")
# print(madrid.filter_by_current_opening_hours())
# print("Paris. filter_by_opening_hours")
# print(paris.filter_by_opening_hours("05/12/2023", "23:45"))
# print("Paris. filter_by_current_opening_hours")
# print(paris.filter_by_current_opening_hours())
# print("New York. filter_by_opening_hours")
# print(new_york.filter_by_opening_hours("05/12/2023", "23:45"))
# print("New York. filter_by_current_opening_hours")
# print(new_york.filter_by_current_opening_hours())
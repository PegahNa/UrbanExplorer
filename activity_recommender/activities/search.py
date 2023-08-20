import json
import datetime

# Custom exception to raise an error if user asks for a rating higher than 5 stars
class RatingHigherThan5Stars(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
        print("self.value ", self.value)

    # __str__ is to print() the value
    def __str__(self):
        return f"The rating {self.value} is not in the range of 1-5 stars"



# Class that will filter all the key-values options on our JSON file
class Filter:
    # Specify to which city user is travelling
    def __init__(self, city):
        self.city = city

    """
    Checks whether activities are within a range of money
    :param target_price: It can either be cheap, medium, expensive or free
    :return: JSON representation of activities within that range price
    """
    def filter_by_price(self, target_price):
        if target_price == "cheap":
            target_price = range(1, 10)
        elif target_price == "medium":
            target_price = range(10, 20)
        elif target_price == "expensive":
            target_price = range(20, 100)
        elif target_price == "free":
            target_price = [0]
        result = [activity for activity in self.city if activity["price"] in target_price]
        return result

    """
    Checks whether activities are within a range of stars (rating)
    :param target_rating: It can either be 0, 1, 2, 3, 4 or 5
    :return: JSON representation of activities within that rating (e.g. 4 stars encompasses 4.0, 4.1, 4.2, 4.3, etc)
    """

    # This should go in utils
    def ratings(self,target_rating):
        if target_rating == 0:
            return [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        if target_rating == 1:
            return [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
        if target_rating == 2:
            return [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]
        if target_rating == 3:
            return [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]
        if target_rating == 4:
            return [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]
        if target_rating == 5:
            return [5]

    def filter_by_rating(self, desired_rating):
        target_rating = self.ratings(desired_rating)
        try:
            if target_rating[0] not in [0, 1, 2, 3, 4, 5.0]:
                raise RatingHigherThan5Stars(target_rating)
            else:
                result = [activity for activity in self.city if activity["rating"] in target_rating]
                return result
        except RatingHigherThan5Stars as err:
            return "The rating requested is not in the range of 1-5 stars", err.value

    def filter_by_wheelchair_accessible_entrance(self):
        result = [activity for activity in self.city if activity["wheelchair_accessible_entrance"] is True]
        return result

    def filter_by_hearing_accessibility(self):
        result = [activity for activity in self.city if activity["hearing_accessibility"] is True]
        return result

    def filter_by_visual_accessibility(self):
        result = [activity for activity in self.city if activity["visual_accessibility"] is True]
        return result

    """
    Filters activities open on a specified future date and time (inputted by user, dates of their holidays).
    :param target_date: The target date in format "dd/mm/yyyy".
    :param target_time: The target time in format "HH:MM".
    :return: JSON representation of open activities on that day and at that time.
    """
    def filter_by_future_opening_hours(self, target_date, target_time):
        date_format = "%d/%m/%Y"
        date_time = "%H:%M"

        # It gets the target day in format "Monday" and the target time in format "12:05"
        day_target = datetime.datetime.strptime(target_date, date_format).strftime("%A")
        time_target = datetime.datetime.strptime(target_time, date_time).strftime("%H:%M")

        result = []

        # For activities open 24hs and activities that much in time and day, append to open_activities
        for activity in self.city:
            if activity["opening_hours"]["everyday"] == "24hs":
                result.append(activity)
            elif activity["opening_hours"]["specific_times"] is not None:
                for opening in activity["opening_hours"]["specific_times"]:
                    if opening["day"] == day_target and opening["open"] <= time_target <= opening["close"]:
                        result.append(activity)
                        break
        return result

    """
    Filters activities that are currently open based on the current day and time.
    :return: JSON representation of open activities.
    """
    def filter_by_current_opening_hours(self):
        current_day = datetime.datetime.now().strftime("%A")
        current_time = datetime.datetime.now().strftime("%H:%M")

        result = []

        for activity in self.city:
            if activity["opening_hours"]["everyday"] == "24hs":
                result.append(activity)
            else:
                specific_times = activity["opening_hours"]["specific_times"]
                if specific_times is not None:
                    for opening in specific_times:
                        if opening["day"] == current_day and opening["open"] <= current_time <= opening["close"]:
                            result.append(activity)
                            break
        return result


    def show_activity_details(self, data):
        for index, activity in enumerate(data, start=1):
            print(f"{index}. {activity['activity']}")
        selected_activity = input("What activity do you choose? Write the number \n")

        activity = data[int(selected_activity)-1]
        print(f"Name: {activity['activity']}")
        print(f"Price: £{activity['price']}")
        print(f"Rating: {activity['rating']} stars")
        print(f"Wheelchair accessible: {('Yes' if activity['wheelchair_accessible_entrance'] else 'No')}")
        print(f"Hearing impaired accessible: {('Yes' if activity['hearing_accessibility'] else 'No')}")
        print(f"Visual impaired accessible: {('Yes' if activity['visual_accessibility'] else 'No')}")
        if activity["opening_hours"]["everyday"] == "24hs":
            print(f"Opening hours: {activity['opening_hours']['everyday']}")
        elif activity["opening_hours"]["everyday"] == "":
            print("Opening hours:")
            for time in activity['opening_hours']['specific_times']:
                print(f"    {time['day']} from {time['open']} to {time['close']}")



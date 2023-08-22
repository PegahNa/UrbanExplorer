from activity_recommender.utils.utils import get_range_of_ratings, get_range_of_prices, euro_or_dollars
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
    def __init__(self, data_city, city):
        self.data_city = data_city
        self.city = city
        self.filtered_results = []

    """
    Checks whether activities are within a range of money
    :param target_price: It can either be cheap, medium, expensive or free
    :return: JSON representation of activities within that range price
    """
    def filter_by_price(self, target_price):
        self.filtered_results = [activity for activity in self.data_city if activity["price"] in get_range_of_prices(target_price)]
        return self.filtered_results

    """
    Checks whether activities are within a range of stars (rating)
    :param target_rating: It can either be 0, 1, 2, 3, 4 or 5
    :return: JSON representation of activities within that rating (e.g. 4 stars encompasses 4.0, 4.1, 4.2, 4.3, etc)
    """
    def filter_by_rating(self, desired_rating):
        target_rating = get_range_of_ratings(desired_rating)
        try:
            if target_rating[0] not in [0, 1, 2, 3, 4, 5.0]:
                raise RatingHigherThan5Stars(target_rating)
            else:
                self.filtered_results = [activity for activity in self.data_city if activity["rating"] in target_rating]
                return self.filtered_results
        except RatingHigherThan5Stars as err:
            return "The rating requested is not in the range of 1-5 stars", err.value

    def filter_by_wheelchair_accessible_entrance(self):
        self.filtered_results = [activity for activity in self.data_city if activity["wheelchair_accessible_entrance"] is True]
        return self.filtered_results

    def filter_by_hearing_accessibility(self):
        self.filtered_results = [activity for activity in self.data_city if activity["hearing_accessibility"] is True]
        return self.filtered_results

    def filter_by_visual_accessibility(self):
        self.filtered_results = [activity for activity in self.data_city if activity["visual_accessibility"] is True]
        return self.filtered_results

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

        # For activities open 24hs and activities that much in time and day, append to open_activities
        for activity in self.data_city:
            if activity["opening_hours"]["everyday"] == "24hs":
                self.filtered_results.append(activity)
            elif activity["opening_hours"]["specific_times"] is not None:
                for opening in activity["opening_hours"]["specific_times"]:
                    if opening["day"] == day_target and opening["open"] <= time_target <= opening["close"]:
                        self.filtered_results.append(activity)
                        break
        return self.filtered_results

    """
    Filters activities that are currently open based on the current day and time.
    :return: JSON representation of open activities.
    """
    def filter_by_current_opening_hours(self):
        current_day = datetime.datetime.now().strftime("%A")
        current_time = datetime.datetime.now().strftime("%H:%M")

        for activity in self.data_city:
            if activity["opening_hours"]["everyday"] == "24hs":
                self.filtered_results.append(activity)
            else:
                specific_times = activity["opening_hours"]["specific_times"]
                if specific_times is not None:
                    for opening in specific_times:
                        if opening["day"] == current_day and opening["open"] <= current_time <= opening["close"]:
                            self.filtered_results.append(activity)
                            break
        return self.filtered_results


    def show_activity_details(self, data):
        for index, activity in enumerate(data, start=1):
            print(f"{index}. {activity['activity']}")

        selected_activity = int(input("What activity do you choose? Write the number \n"))

        number_of_options = list(range(1, len(data) + 1))
        if selected_activity in number_of_options:
            activity = data[selected_activity-1]
            print(f"Name: {activity['activity']}")
            print(f"Price: {euro_or_dollars(self.city)}{activity['price']}")
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
        else:
            print(f"Invalid input. It can only be {', '.join(map(str, number_of_options))}")
            self.show_activity_details(data)



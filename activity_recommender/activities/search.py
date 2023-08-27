from activity_recommender.utils.search_utils import get_range_of_ratings, get_range_of_prices, euro_or_dollars
import datetime


# Custom exception to raise an error if user asks for a rating higher than 5 stars
class RatingHigherThan5Stars(Exception):
    pass


class PriceNotInOptions(Exception):
    pass


class ActivityNotInOptions(Exception):
    pass


# Class that will filter all the key-values options activities data (JSON file)
class Filter:
    # Get data from specific city, get name for chosen city and filtered results
    # (that at first, they'll be the same as data city, as they haven't been filtered yet)
    def __init__(self, data_city, city):
        self.data_city = data_city
        self.city = city
        self.filtered_results = data_city

    """
    Checks whether activities are within a range of money
    :param target_price: It can either be cheap, medium, expensive or free
    :return: JSON representation of activities within that range price
    """
    def filter_by_price(self, target_price):
        desired_rating = get_range_of_prices(target_price)
        try:
            if desired_rating is None:
                raise PriceNotInOptions
            else:
                self.filtered_results = [activity for activity in self.filtered_results if activity["price"] in desired_rating]
                # pretty_result = json.dumps(self.filtered_results, indent=4)
                return self.filtered_results
        except PriceNotInOptions:
            return "The price requested is not possible. It can only be free, cheap, medium or expensive "

    """
    Checks whether activities are within a range of stars (rating)
    :param target_rating: It can either be 0, 1, 2, 3, 4 or 5
    :return: JSON representation of activities within that rating (e.g. 4 stars encompasses 4.0, 4.1, 4.2, 4.3, etc)
    """
    def filter_by_rating(self, target_rating):
        desired_rating = get_range_of_ratings(target_rating)
        try:
            if desired_rating is None:
                raise RatingHigherThan5Stars
            else:
                self.filtered_results = [activity for activity in self.filtered_results if activity["rating"] in desired_rating]
                # pretty_result = json.dumps(self.filtered_results, indent=4)
                return self.filtered_results
        except RatingHigherThan5Stars:
            return "The rating requested is not in the range of 1-5 stars"

    # Checks whether activities have accessible entrance
    def filter_by_wheelchair_accessible_entrance(self):
        self.filtered_results = [activity for activity in self.filtered_results if activity["wheelchair_accessible_entrance"] is True]
        return self.filtered_results

    # Checks whether activities have accessible to hearing impaired people
    def filter_by_hearing_accessibility(self):
        self.filtered_results = [activity for activity in self.filtered_results if activity["hearing_accessibility"] is True]
        return self.filtered_results

    # Checks whether activities have accessible to visually impaired people
    def filter_by_visual_accessibility(self):
        self.filtered_results = [activity for activity in self.filtered_results if activity["visual_accessibility"] is True]
        return self.filtered_results

    """
    Filters activities open on a specified future date and time.
    :param target_date: The target date in format "dd/mm/yyyy".
    :param target_time: The target time in format "HH:MM".
    :return: JSON representation of open activities on that day and at that time.
    """
    def filter_by_future_opening_hours(self, target_date, target_time):
        date_format = "%d/%m/%Y"
        date_time = "%H:%M"

        try:
            # It gets the target day in format "Monday" and the target time in format "12:05"
            day_target = datetime.datetime.strptime(target_date, date_format).strftime("%A")
            time_target = datetime.datetime.strptime(target_time, date_time).strftime("%H:%M")

            list_of_activities = []

            # For activities open 24hs and activities that match in day and time, append to open_activities
            for activity in self.filtered_results:
                if activity["opening_hours"]["everyday"] == "24hs":
                    list_of_activities.append(activity)
                elif activity["opening_hours"]["specific_times"] is not None:
                    for opening in activity["opening_hours"]["specific_times"]:
                        if opening["day"] == day_target and opening["open"] <= time_target <= opening["close"]:
                            list_of_activities.append(activity)
                            break
            self.filtered_results = list_of_activities
            return self.filtered_results
        except ValueError:
            return "Time and day are not valid. Please, check the format"

    """
    Filters activities that are currently open based on the current day and time.
    :return: JSON representation of open activities.
    """
    def filter_by_current_opening_hours(self):
        current_day = datetime.datetime.now().strftime("%A")
        current_time = datetime.datetime.now().strftime("%H:%M")

        list_of_activities = []

        for activity in self.filtered_results:
            if activity["opening_hours"]["everyday"] == "24hs":
                list_of_activities.append(activity)
            else:
                specific_times = activity["opening_hours"]["specific_times"]
                if specific_times is not None:
                    for opening in specific_times:
                        if opening["day"] == current_day and opening["open"] <= current_time <= opening["close"]:
                            list_of_activities.append(activity)
                            break

        self.filtered_results = list_of_activities
        return self.filtered_results

    def show_activity_details(self):
        for index, activity in enumerate(self.filtered_results, start=1):
            print(f"{index}. {activity['activity']}")

        selected_activity = int(input("What activity do you choose? Write the number \n"))
        print("")

        number_of_options = list(range(1, len(self.filtered_results) + 1))
        try:
            if selected_activity in number_of_options:

                activity = self.filtered_results[selected_activity-1]
                activity_selected = activity['activity']

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
                return activity_selected
            else:
                raise ActivityNotInOptions
        except ActivityNotInOptions:
            print(f"Invalid input. It can only be {', '.join(map(str, number_of_options))}")
            self.show_activity_details()

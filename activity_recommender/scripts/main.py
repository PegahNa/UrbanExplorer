import json
from datetime import datetime
import os
# Changed import path
from activity_recommender.activities.search import Filter
# adding login import
from activity_recommender.auth.login import UserManager, User, ExistingUserError
from activity_recommender.utils.main_utils import print_filters_used, get_filter_from_numbers
from activity_recommender.API.api_integration import main


#  We need to do error handling for every function and a back function for each menu
class UserRetrievalError(Exception):
    pass


class UserLoginError(Exception):
    pass


class ActivityRecommender:
    def __init__(self):
        self.locations_data = self.load_locations_data()
        self.city = None
        self.filter_obj = None
        self.filters_applied = []
        self.filtered_results = []

    def load_locations_data(self):
        # Changed path so it'd work
        location_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "locations.json")
        with open(location_file) as json_file:
            data = json.load(json_file)
        return data

    # updating the main menu function for login
    def main_menu(self):

        # initialising the user manage for managing users
        user_manager = UserManager()

        # try retrieving any existing users from the file, raise an error if the users weren't retrieved
        try:
            user_manager.retrieve_users()
        except UserRetrievalError as e:
            print(f"Custom Exception Caught: {e}")

        # making sure the user logs in or registers before seeing the rest of the options
        choice = input("Welcome, please choose an option:\n1. Login\n2. Register\n3. Exit\n")
        # handling user's choice for login
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            # creating an instance of user
            user = User(username, password)
            if user.login():
                print("Login successful\n")
                while True:
                    choice = input("\n----MENU----\n1. Search Activities\n2. Logout\n")
                    if choice == "1":
                        self.choose_activity()
                    elif choice == "2":
                        print(user.logout())
                        exit()
                    else:
                        print("Invalid choice, please choose from option 1 or 2: ")
                        continue
            else:
                print("Incorrect username or password")
                self.main_menu()

        # handling a users choice for registration
        elif choice == "2":
            username = input("Enter a username:")
            password = input("Enter a password: ")
            # creating an instance of the user
            new_user = User(username, password)
            # add error handling to handle if the user does exist when the user registers
            try:
                user_manager.add_user(new_user)
                print("Registration successful, you can now login")
                self.main_menu()
            except ExistingUserError:
                print("Username already. Please register again with a different one.")
                self.main_menu()

        # handling a users choice to exit
        elif choice == "3":
            exit()

        # handling invalid choices
        else:
            print("Invalid selection")
            self.main_menu()

    def choose_activity(self):
        self.city = input("\nEnter the city you're traveling to (Madrid, Paris or New York): \n").lower()
        print("")
        city_options = ["madrid", "paris", "new york"]
        if self.city in city_options:
            self.filter_obj = Filter(self.locations_data[self.city], self.city)
            self.choose_more_than_one_filter()
            # self.search_activities_menu()
        else:
            print("Invalid choice. \n")
            self.choose_activity()

    """ 
    Function to apply all the filters chosen.
    It takes a list of methods selected by user and applies one by one
    :param methods: list of name of methods
    """
    def apply_filters(self, methods):
        for method_name in methods:
            method = getattr(self, method_name)
            method()

    # This needs error handling
    def choose_more_than_one_filter(self):
        # Erase history of filters chosen each time you call this function


        print("1. Filter by Price")
        print("2. Filter by Rating")
        print("3. Filter by Accessibility")
        print("4. Filter by Opening Hours \n")
        filters_chosen = input("Select all the filters you want to apply, separated by a comma (e.g. 1, 2, 3) \n")

        # Gets a list of numbers selected by user (e.g. ["1", "3", "4"])
        filters_chosen = list(filters_chosen.split(", "))
        # Using a utils function, it gets a list of the names of those filters (e.g. ["search_by_price", "search_by_accessibility", "search_by_opening_hours"])
        filters_to_apply = get_filter_from_numbers(filters_chosen)

        # Applies each filter by calling self.name_of_method()
        self.apply_filters(filters_to_apply)

        # It will show all the results obtained
        self.show_activities()


    def search_by_price(self):
        target_price = input("Enter the target price: cheap, medium, expensive or free: \n").lower()
        price_options = ["cheap", "medium", "expensive", "free"]
        if target_price in price_options:
            self.filtered_results = self.filter_obj.filter_by_price(target_price)
            self.filters_applied.append({"filter_by_price()": target_price})
        else:
            print("Invalid choice.")
            self.search_by_price()

    def search_by_rating(self):
        try:
            target_rating = int(input("Enter the target rating (1 to 5): \n"))
            rating_options = [1, 2, 3, 4, 5]
            if target_rating in rating_options:
                self.filtered_results = self.filter_obj.filter_by_rating(int(target_rating))
                self.filters_applied.append({"filter_by_rating()": target_rating})
            else:
                print("Invalid choice.")
                self.search_by_rating()
        except ValueError:
            print("Wrong input. It needs to be a number.")
            self.search_by_rating()

    # Fixed issue with indentation
    def search_by_accessibility(self):
        print("1. Wheelchair Accessible Entrance")
        print("2. Hearing Accessibility")
        print("3. Visual Accessibility")
        print("4. Go back to search by filters menu \n")

        accessibility_choice = input("Please select an accessibility option: \n")

        if accessibility_choice == "1":
            self.filtered_results = self.filter_obj.filter_by_wheelchair_accessible_entrance()
            self.filters_applied.append({"filter_by_wheelchair_accessible_entrance()": ""})
            #self.show_activities(result)
        elif accessibility_choice == "2":
            self.filter_obj.filter_by_hearing_accessibility()
            self.filters_applied.append({"filter_by_hearing_accessibility()": ""})
            #self.show_activities(result)
        elif accessibility_choice == "3":
            self.filter_obj.filter_by_visual_accessibility()
            self.filters_applied.append({"filter_by_visual_accessibility()": ""})
            #self.show_activities(result)
        elif accessibility_choice == "4":
            self.choose_more_than_one_filter()
        else:
            print("Invalid choice. \n")
            self.search_by_accessibility()

    def search_by_opening_hours(self):
        print("1. Search by Current Opening Hours")
        print("2. Search by Specific Date and Time")
        print("3. Go back to search by filters menu \n")

        opening_hours_choice = input("Please select an opening hours option: \n")

        if opening_hours_choice == "1":
            self.filter_obj.filter_by_current_opening_hours()
            self.filters_applied.append({"filter_by_current_opening_hours()": ""})
            #self.show_activities(result)
        elif opening_hours_choice == "2":
            while True:
                target_date = input("Enter the date you're going to travel (dd/mm/yyyy): ")
                target_time = input("Enter the time you're going to travel (hh:mm): ")
                try:
                    datetime.strptime(target_date, "%d/%m/%Y")
                    datetime.strptime(target_time, "%H:%M")
                    self.filter_obj.filter_by_future_opening_hours(target_date, target_time)
                    self.filters_applied.append({"filter_by_future_opening_hours()": f"Date: {target_date}. Time: {target_time}."})
                    #self.show_activities(result)
                    break
                except ValueError:
                    print("Wrong format. Please provide the date in dd/mm/yyyy and the time in hh:mm format.")
        elif opening_hours_choice == "3":
            self.choose_more_than_one_filter()
        else:
            print("Invalid choice.")
            self.search_by_opening_hours()

    def show_activities(self):
        if not self.filtered_results:
            print("There are not results for that option")
            self.choose_more_than_one_filter()
        else:
            while True:
                name_of_activity = self.filter_obj.show_activity_details()
                print(name_of_activity)
                filter_chosen = print_filters_used(self.filters_applied)
                print("\n Menu")
                print("1. Go to map of activity")
                print("2. Go back to list of activities")
                print("3. Go to search by filter menu and change your filters \n")
                print(f"Filters selected at the moment: ")

                for filter in filter_chosen:
                    print(filter)

                map_or_list = input("\nChoose an option (write the number) \n")

                if map_or_list == "1":
                    # function to show map
                    print(main(name_of_activity))
                    exit()
                elif map_or_list == "2":
                    continue
                elif map_or_list == "3":
                    self.filters_applied.clear()
                    self.filtered_results.clear()
                    self.filter_obj = Filter(self.locations_data[self.city], self.city)
                    self.choose_more_than_one_filter()
                else:
                    print("Invalid input.")

    def main(self):
        self.main_menu()


if __name__ == "__main__":
    recommender = ActivityRecommender()
    recommender.main()

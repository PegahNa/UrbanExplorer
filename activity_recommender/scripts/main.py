import json
from datetime import datetime
import os
from activity_recommender.activities.search import Filter
from activity_recommender.auth.login import UserManager, User, ExistingUserError
from activity_recommender.utils.main_utils import print_filters_used, get_filter_from_numbers
from activity_recommender.API.api_integration import get_url


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

    # Import activity data of Madrid, Paris and New York that will be filtered
    def load_locations_data(self):
        location_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "locations.json")
        with open(location_file) as json_file:
            data = json.load(json_file)
        return data

    # Main menu that user will have access to once the program starts running
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
            try:
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
                    raise UserLoginError
            except UserLoginError:
                print("Incorrect username or password, please try again or register again")
                self.main_menu()

        # handling a users choice for registration
        elif choice == "2":
            username = input("Enter a username: ")
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

    # Menu to choose city user is travelling to. It will take you to a menu to filter activities in each city
    def choose_activity(self):
        self.city = input("\nEnter the city you're travelling to (Madrid, Paris or New York): \n").lower()
        print("")
        city_options = ["madrid", "paris", "new york"]
        try:
            # Initiate an object of the data specific to city chosen
            if self.city in city_options:
                self.filter_obj = Filter(self.locations_data[self.city], self.city)
                self.filter_activities()
            else:
                raise ValueError
        except ValueError:
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

    # Menu to choose filters to apply to data. It can be multiple filters at the same time
    def filter_activities(self):
        print("Filters menu")
        print("1. Filter by Price")
        print("2. Filter by Rating")
        print("3. Filter by Accessibility")
        print("4. Filter by Opening Hours \n")
        filters_chosen = input("Select all the filters you want to apply, separated by a comma (e.g. 1, 3, 4) \n")

        possible_options = ["1", "2", "3", "4"]

        # Gets a list of numbers selected by user (e.g. ["1", "3", "4"])
        filters_chosen = list(filters_chosen.split(", "))

        try:
            # Check whether input is within possible options in the menu
            if set(filters_chosen).issubset(set(possible_options)):

                # Using a utils function, it gets a list of the names of those filters (e.g. ["search_by_price", "search_by_accessibility", "search_by_opening_hours"])
                filters_to_apply = get_filter_from_numbers(filters_chosen)

                # Applies each filter by calling self.name_of_method()
                self.apply_filters(filters_to_apply)

                # It will show all the results obtained
                self.show_activities()
            else:
                raise ValueError
        except ValueError:
            print("Invalid input \n")
            self.filter_activities()

    # It filters the activities of selected city according to a range of prices
    def search_by_price(self):
        print("Price filter")
        target_price = input("Enter the target price: cheap, medium, expensive or free: \n").lower()
        price_options = ["cheap", "medium", "expensive", "free"]
        try:
            if target_price in price_options:
                # It filters activities by target price and it keeps track of which filter has been chosen
                self.filtered_results = self.filter_obj.filter_by_price(target_price)
                self.filters_applied.append({"filter_by_price()": target_price})
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. \n")
            self.search_by_price()

    # It filters the activities of selected city according to a range of ratings
    def search_by_rating(self):
        try:
            print("Rating filter")
            target_rating = int(input("Enter the target rating of stars (1 to 5): \n"))
            rating_options = [1, 2, 3, 4, 5]
            if target_rating in rating_options:
                self.filtered_results = self.filter_obj.filter_by_rating(int(target_rating))
                self.filters_applied.append({"filter_by_rating()": target_rating})
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. \n")
            self.search_by_rating()

    # It filters the activities of selected city according to accessibility
    def search_by_accessibility(self):
        print("Accessibility filter")
        print("1. Wheelchair Accessible Entrance")
        print("2. Hearing Accessibility")
        print("3. Visual Accessibility")
        print("4. Go back to search by filters menu \n")

        accessibility_choice = input("Please select an accessibility option (1, 2, 3 or 4): \n")

        possible_options = ["1", "2", "3", "4"]

        try:
            if accessibility_choice in possible_options:
                if accessibility_choice == "1":
                    self.filtered_results = self.filter_obj.filter_by_wheelchair_accessible_entrance()
                    self.filters_applied.append({"filter_by_wheelchair_accessible_entrance()": ""})
                elif accessibility_choice == "2":
                    self.filter_obj.filter_by_hearing_accessibility()
                    self.filters_applied.append({"filter_by_hearing_accessibility()": ""})
                elif accessibility_choice == "3":
                    self.filter_obj.filter_by_visual_accessibility()
                    self.filters_applied.append({"filter_by_visual_accessibility()": ""})
                elif accessibility_choice == "4":
                    self.filter_activities()
                else:
                    raise ValueError
        except ValueError:
            print("Invalid choice. \n")
            self.search_by_accessibility()

    # It filters the activities of selected city according to opening hours
    def search_by_opening_hours(self):
        print("Opening hours filter")
        print("1. Search by Current Opening Hours")
        print("2. Search by Specific Date and Time")
        print("3. Go back to search by filters menu \n")

        possible_options = ["1", "2", "3"]

        opening_hours_choice = input("Please select an opening hours option (1, 2 or 3): \n")

        try:
            if opening_hours_choice in possible_options:
                if opening_hours_choice == "1":
                    self.filter_obj.filter_by_current_opening_hours()
                    self.filters_applied.append({"filter_by_current_opening_hours()": ""})
            elif opening_hours_choice == "2":
                while True:
                    target_date = input("Enter the date you're going to travel (dd/mm/yyyy): ")
                    target_time = input("Enter the time you're going to travel (hh:mm): ")
                    try:
                        datetime.strptime(target_date, "%d/%m/%Y")
                        datetime.strptime(target_time, "%H:%M")
                        self.filter_obj.filter_by_future_opening_hours(target_date, target_time)
                        self.filters_applied.append({"filter_by_future_opening_hours()": f"Date: {target_date}. Time: {target_time}."})
                        break
                    except ValueError:
                        print("Wrong format. Please provide the date in dd/mm/yyyy and the time in hh:mm format. \n")
            elif opening_hours_choice == "3":
                self.filter_activities()
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. \n")
            self.search_by_opening_hours()

    # It will show a list of filtered activities
    def show_activities(self):
        if not self.filtered_results:
            print("There are not results for that option \n")
            self.filter_activities()
        else:
            while True:
                # It prints a list of names of activities, it lets user choose which activity they want to choose and it shows the specific details of that activity
                name_of_activity = self.filter_obj.show_activity_details()

                # It creates a list of the filters applied to the data in a format readable by user
                filter_chosen = print_filters_used(self.filters_applied)
                print("\n Menu")
                print("1. Go to map of activity")
                print("2. Go back to list of activities")
                print("3. Go to search by filter menu and change your filters \n")
                print(f"Filters selected at the moment: ")

                for filter in filter_chosen:
                    print(filter)

                map_or_list = input("\nChoose an option (1, 2 or 3): \n")

                possible_options = ["1", "2", "3"]
                try:
                    if map_or_list in possible_options:
                        if map_or_list == "1":
                            # This will show a URL for the activity address
                            print(get_url(name_of_activity))
                            exit()
                        # It will go back to the list of activities
                        elif map_or_list == "2":
                            continue
                        elif map_or_list == "3":
                            # Erase history of previous filters chosen and filter activities according to new filters
                            self.filters_applied.clear()
                            self.filtered_results.clear()
                            self.filter_obj = Filter(self.locations_data[self.city], self.city)
                            self.filter_activities()
                        else:
                            raise ValueError
                except ValueError:
                    print("Invalid input. \n")
                    self.show_activities()

    def main(self):
        self.main_menu()


if __name__ == "__main__":
    recommender = ActivityRecommender()
    recommender.main()

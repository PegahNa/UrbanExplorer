import json
from datetime import datetime
import os
# Changed import path
from activity_recommender.activities.search import Filter
# adding login import
from activity_recommender.auth.login import UserManager, User, ExistingUserError

#  We need to do error handling for every function and a back function for each menu


class ActivityRecommender:
    def __init__(self):
        self.locations_data = self.load_locations_data()
        self.city = None
        self.filter_obj = None

    def load_locations_data(self):
        # Changed path so it'd work
        location_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "locations.json")
        with open(location_file) as json_file:
            data = json.load(json_file)
        return data

    # Don't think we need this function...
    def save_locations_data(self):
        with open('data/locations.json', 'w') as json_file:
            json.dump(self.locations_data, json_file, indent=4)

    # updating the main menu function for login
    def main_menu(self):

        # initialising the user manage for managing users
        user_manager = UserManager()
        # retrieving any existing users from the file
        user_manager.retrieve_users()

        # making sure the user logs in or registers before seeing the rest of the options
        choice = input("Welcome, please choose an option:\n1. Login\n2. Register\n3. Exit\n")
        # handling user's choice for login
        if choice == "1":
            username = input("Enter username: ")  # TODO: LIVVY TO CHECK
            password = input("Enter password: ")
            # creating an instance of user
            user = User(username, password)
            if user.login():
                print("Login successful\n")
                # TODO: Add the menu and options to search
                choice = input("\n----MENU----\n1. Search Activities\n2. Logout\n") #TODO can we use choice for var name
                if choice == "1":
                    self.choose_activity()
                elif choice == "2":
                    print(user.logout())
                    exit()
                else:
                    print("Invalid choice!")
                    self.main_menu()  # TODO: This needs to be updated to not go the first main menu
            else:
                print("Incorrect username or password")
                self.main_menu()

        # handling a users choice for registration
        elif choice == "2":
            username = input("Enter a username:")
            password = input("Enter a password: ")  # TODO: probably worth asking password twice?
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
            self.search_activities_menu()
        else:
            print("Invalid choice. \n")
            self.choose_activity()

    def search_activities_menu(self):
        print("1. Filter by Price")
        print("2. Filter by Rating")
        print("3. Filter by Accessibility")
        print("4. Filter by Opening Hours")
        print("5. Go back to the main menu \n")

        search_choice = input("Please select a search option: \n")
        # I should make this a function in utils
        if search_choice == "1":
            self.search_by_price()
        elif search_choice == "2":
            self.search_by_rating()
        elif search_choice == "3":
            self.search_by_accessibility()
        elif search_choice == "4":
            self.search_by_opening_hours()
        elif search_choice == "5":
            self.main_menu()
        else:
            print("Invalid choice.")
            self.search_activities_menu()

    # Modified parameters to fit the methods of Filter class
    def search_by_price(self):
        target_price = input("Enter the target price: cheap, medium, expensive or free: \n").lower()
        price_options = ["cheap", "medium", "expensive", "free"]
        if target_price in price_options:
            result = self.filter_obj.filter_by_price(target_price)
            self.show_activities(result)
        else:
            print("Invalid choice.")
            self.search_by_price()

    def search_by_rating(self):
        try:
            target_rating = int(input("Enter the target rating (1 to 5): \n"))
            rating_options = [1, 2, 3, 4, 5]
            if target_rating in rating_options:
                result = self.filter_obj.filter_by_rating(int(target_rating))
                self.show_activities(result)
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
        print("4. Go back to search menu \n")

        accessibility_choice = input("Please select an accessibility option: \n")

        if accessibility_choice == "1":
            result = self.filter_obj.filter_by_wheelchair_accessible_entrance()
            self.show_activities(result)
        elif accessibility_choice == "2":
            result = self.filter_obj.filter_by_hearing_accessibility()
            self.show_activities(result)
        elif accessibility_choice == "3":
            result = self.filter_obj.filter_by_visual_accessibility()
            self.show_activities(result)
        elif accessibility_choice == "4":
            self.search_activities_menu()
        else:
            print("Invalid choice. \n")
            self.search_by_accessibility()

    def search_by_opening_hours(self):
        print("1. Search by Current Opening Hours")
        print("2. Search by Specific Date and Time")
        print("3. Go back to search menu \n")

        opening_hours_choice = input("Please select an opening hours option: \n")

        if opening_hours_choice == "1":
            result = self.filter_obj.filter_by_current_opening_hours()
            self.show_activities(result)
        elif opening_hours_choice == "2":
            while True:
                target_date = input("Enter the date you're going to travel (dd/mm/yyyy): ")
                target_time = input("Enter the time you're going to travel (hh:mm): ")
                try:
                    datetime.strptime(target_date, "%d/%m/%Y")
                    datetime.strptime(target_time, "%H:%M")
                    result = self.filter_obj.filter_by_future_opening_hours(target_date, target_time)
                    self.show_activities(result)
                    break
                except ValueError:
                    print("Wrong format. Please provide the date in dd/mm/yyyy and the time in hh:mm format.")
        elif opening_hours_choice == "3":
            self.search_activities_menu()
        else:
            print("Invalid choice.")
            self.search_by_opening_hours()

    def show_activities(self, filtered_activities):
        if not filtered_activities:
            print("There are not results for that option")
            self.search_activities_menu()
        else:
            while True:
                self.filter_obj.show_activity_details(filtered_activities)

                print("\n Menu")
                print("1. Go to map of activity")
                print("2. Go back to list of activities")
                print("3. Go to filters menu")

                map_or_list = input("Choose an option (write the number) \n")

                if map_or_list == "1":
                    # function to show map
                    print("map")
                    exit()
                elif map_or_list == "2":
                    continue
                elif map_or_list == "3":
                    self.search_activities_menu()
                else:
                    print("Invalid input.")

    def main(self):
        self.main_menu()


if __name__ == "__main__":
    recommender = ActivityRecommender()
    recommender.main()
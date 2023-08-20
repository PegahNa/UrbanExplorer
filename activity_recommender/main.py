import json
# Changed import path
from activities.search import Filter
# import login


class ActivityRecommender:
    def __init__(self):
        self.locations_data = self.load_locations_data()

    def load_locations_data(self):
        # Changed path so it'd work
        with open('../data/locations.json') as json_file:
            data = json.load(json_file)
        return data

    # All the methods related to login should be imported, not defined
    def get_user(self, username):
        if username in self.locations_data['users']:
            return self.locations_data['users'][username]
        return None

    def login(self):
        username = input("Username: ")
        user = self.get_user(username)
        if user:
            password = input("Password: ")
            while password != user['password']:
                print("Incorrect password. Please try again.")
                password = input("Password: ")
            print("Login successful!")
            return True
        else:
            print("User not found. Please register.")
            return False

    def register(self):
        username = input("Enter a username: ")
        if self.get_user(username):
            print("Username already exists. Please choose a different one.")
            return
        password = input("Enter a password: ")
        self.locations_data['users'][username] = {'password': password}
        self.save_locations_data()
        print("Registration successful!")

    def save_locations_data(self):
        with open('data/locations.json', 'w') as json_file:
            json.dump(self.locations_data, json_file, indent=4)

    def main_menu(self):
        print("Welcome to Activity Recommender!")
        print("1. Login")
        print("2. Register")
        print("3. Search Activities")
        print("4. Admin Functions (Admin Only)")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            self.search_activities_menu()
        elif choice == "4":
            self.admin_functions()
        elif choice == "5":
            # This counts as recursivity, right? haha
            exit()
        else:
            print("Invalid choice!")
            self.main_menu()

    def search_activities_menu(self):
        filter_city = input("Enter the city you're traveling to: ").lower()
        # Need error handling for this (incorrect name city)
        # Changed the function to make it work
        filter_obj = Filter(self.locations_data[filter_city])

        print("1. Filter by Price")
        print("2. Filter by Rating")
        print("3. Filter by Accessibility")
        print("4. Filter by Opening Hours")
        print("5. Go back to the main menu")

        search_choice = input("Please select a search option: ")

        if search_choice == "1":
            self.search_by_price(filter_obj)
        elif search_choice == "2":
            self.search_by_rating(filter_obj)
        elif search_choice == "3":
            self.search_by_accessibility(filter_obj)
        elif search_choice == "4":
            self.search_by_opening_hours(filter_obj)
        elif search_choice == "5":
            self.main_menu()
        else:
            print("Invalid choice!")
            self.search_activities_menu()

    # Modified parameters to fit the methods of Filter class
    def search_by_price(self, filter_obj):
        target_price = input("Enter the target price: cheap, medium, expensive or free: ")
        result = filter_obj.filter_by_price(target_price)

        while True:
            filter_obj.show_activity(result)

            map_or_list = input("Do you want to see the map for that activity (map) or go back to the list of activities (list)? \n").lower()

            if map_or_list == "map":
                # function to show map
                print("map")
                break
            elif map_or_list == "list":
                continue
            else:
                print("Invalid input. Please enter 'map' or 'list'.")


    def search_by_rating(self, filter_obj):
        target_rating = int(input("Enter the target rating (1 to 5): "))
        result = filter_obj.filter_by_rating([target_rating])
        print(result)

    # Fixed issue with indentation
    def search_by_accessibility(self, filter_obj):
        print("1. Wheelchair Accessible Entrance")
        print("2. Hearing Accessibility")
        print("3. Visual Accessibility")
        print("4. Go back to search menu")

        accessibility_choice = input("Please select an accessibility option: ")

        if accessibility_choice == "1":
            result = filter_obj.filter_by_wheelchair_accessible_entrance()
            print(result)
        elif accessibility_choice == "2":
            result = filter_obj.filter_by_hearing_accessibility()
            print(result)
        elif accessibility_choice == "3":
            result = filter_obj.filter_by_visual_accessibility()
            print(result)
        elif accessibility_choice == "4":
            self.search_activities_menu()
        else:
            print("Invalid choice!")
            self.search_by_accessibility(filter_obj)

    def search_by_opening_hours(self, filter_obj):
        print("1. Search by Current Opening Hours")
        print("2. Search by Specific Date and Time")
        print("3. Go back to search menu")

        opening_hours_choice = input("Please select an opening hours option: ")

        if opening_hours_choice == "1":
            result = filter_obj.filter_by_current_opening_hours()
            print(result)
        elif opening_hours_choice == "2":
            target_date = input("Enter the target date (dd/mm/yyyy): ")
            target_time = input("Enter the target time (hh:mm): ")
            result = filter_obj.filter_by_opening_hours(target_date, target_time)
            print(result)
        elif opening_hours_choice == "3":
            self.search_activities_menu()
        else:
            print("Invalid choice!")
            self.search_by_opening_hours(filter_obj)

    # def show_activity(self, data):
    #     selected_activity = input("What activity do you choose? \n")
    #     for activity in data:
    #         if activity["activity"] == selected_activity:
    #             print(f"Name: {activity['activity']}")
    #             print(f"Price: £{activity['price']}")
    #             print(f"Rating: {activity['rating']} stars")
    #             print(f"Wheelchair accessible: {activity['wheelchair_accessible_entrance']}")
    #             print(f"Hearing impaired accessible: {activity['hearing_accessibility']}")
    #             print(f"Visual impaired accessible: {activity['visual_accessibility']}")
    #             if activity["opening_hours"]["everyday"] == "24hs":
    #                 print(f"Opening hours: {activity['opening_hours']['everyday']}")
    #             elif activity["opening_hours"]["everyday"] == "":
    #                 print("Opening hours:")
    #                 for time in activity['opening_hours']['specific_times']:
    #                     print(f"    {time['day']} from {time['open']} to {time['close']}")
                    #print(f"Opening hours: {activity['opening_hours']['specific_times']}")


    # def admin_functions(self):
    #     print("Admin Functions Menu")
    #     print("1. Add User")
    #     print("2. Remove User")
    #     print("3. View User List")
    #     choice = input("Select an option: ")
    #
    #     if choice == "1":
    #         username = input("Enter username: ")
    #         password = input("Enter password: ")
    #         new_user = User(username, password)
    #         try:
    #             UserManager.add_user(new_user)
    #             print("User added successfully.")
    #         except ExistingUserError:
    #             print("User already exists.")
    #         except UserValidationError:
    #             print("Invalid user details.")
    #
    #     elif choice == "2":
    #         username = input("Enter username to remove: ")
    #         password = input("Enter password: ")
    #         user = self.get_user(username)
    #
    #         if user and password == user['password']:
    #             if UserManager.remove_user(username):
    #                 print("User removed successfully.")
    #             else:
    #                 print("User not found.")
    #         else:
    #             print("Invalid username or password.")
    #
    #     elif choice == "3":
    #         print("User List:")
    #         for username in UserManager.users.keys():
    #             print(username)
    #
    #     else:
    #         print("Invalid choice.")

    def main(self):
        self.main_menu()


if __name__ == "__main__":
    recommender = ActivityRecommender()
    recommender.main()





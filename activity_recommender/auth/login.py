import json
import os

# initialise custom errors
class UserManagerError(Exception):
    pass


class UserValidationError(UserManagerError):
    pass


class ExistingUserError(UserManagerError):
    pass


# initialise class for user management
class UserManager:
    users = {}  # dict to store the list of users, key for username, user object for value
    user_file = r"C:\Coding\Group-1-activity-recommender\data\users.json"

    # method to take users from file and store them in users dict
    @classmethod
    def retrieve_users(cls):
        # check if the file exists and return string if not
        if not os.path.exists(cls.user_file):
            raise FileNotFoundError(f"File {cls.user_file} does not exist. Exiting program")

        try:
            with open(cls.user_file, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            raise UserManagerError(f"Error decoding")

        for username, user_data in data.items():
            user = User(user_data["username"], user_data["password"])
            cls.users[username] = user
        return True  # TODO use this to say that the users have been retrieved and are in users

    # method to save user in the user dict to file TODO double check w is ok since all users will be in user sdict
    @classmethod
    def save_users(cls):
        try:
            with open(cls.user_file, "w") as file:
                users_to_store = {username: {"username": user.username, "password": user.password}
                                  for username, user in cls.users.items()}
                json.dump(users_to_store, file)
        except IOError:
            raise UserManagerError(f"Error writing to {cls.user_file} user cannot be saved and will not be able to log"
                                   f"in next time.")

    # add new user to user dict

    @classmethod
    def add_user(cls, user):
        if not user.username or not user.password:
            raise UserValidationError("Username and password should not be empty.")
        if user.username in cls.users:
            raise ExistingUserError("Username already exists.")
        cls.users[user.username] = user
        cls.save_users()  #TODO would it be better to do this add_user without calling save_user
        return True

    # get users stored in the dict that have been retrieved from the file
    @classmethod
    def get_user(cls, username):
        return cls.users.get(username, None)  # none being the value returned if the username doesn't exist


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        existing_user = UserManager.get_user(self.username)
        if existing_user and existing_user.password == self.password:
            return True  # added this as boolean values, so it's easier for you to use in main.py @Pegah
        else:
            return False  # TODO think about having a while loop at the stage of asking for the password in main.py

    def change_password(self, new_password):
        self.password = new_password
        return "Password has successfully been updated"

    @staticmethod
    def logout():
        return "You have successfully been logged out"


class AdminUser(User):
    # will inherit all things from user class
    # need to return to this once we have created the admin section to see if more is needed
    pass


# # testing if this work

# retrieve users needs to be run to gather all the data into the users dict in UserManager
# UserManager.retrieve_users()
#
# # Testing if the login functionality works
# username_1 = input("Please enter your username: ")  # use livvy.w23
# password_1 = input("Please enter a password: ")  # user cheese
#
# user_1 = User(username_1, password_1)
#
# print(os.getcwd())
# print(user_1.login())  # this should output login successful, however I keep getting login failed
#
# response = UserManager.add_user(user_1)
#
# if response:
#     print("New user successfully registered")

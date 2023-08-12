import json
import os


# initialise class for user management
class UserManager:
    users = {}  # dict to store the list of users, key for username, user object for value
    user_file = "./data/users.json"

    # method to take users from file and store them in users dict
    @classmethod
    def retrieve_users(cls):
        # check if the file exists and return string if not
        if not os.path.exists(cls.user_file):
            return f"File {cls.user_file} does not exist"

        with open(cls.user_file, "r") as file:
            data = json.load(file)
            for username, user_data in data.items():
                user = User(user_data["username"], user_data["password"])
                cls.users[username] = user
        return True  # TODO use this to say that the users have been retrieved and are in users

    # method to save user in the user dict to file TODO double check w is ok since all users will be in user sdict
    @classmethod
    def save_users(cls):
        with open(cls.user_file, "w") as file:
            users_to_store = {username: {"username": user.username, "password": user.password}
                              for username, user in cls.users.items()}
            json.dump(users_to_store, file)

    # add new user to user dict

    @classmethod
    def add_user(cls, user):
        if user.username in cls.users:
            # "Username already exists"  # TODO make sure to add in running of programme, if false user exists
            return False
        else:
            cls.users[user.username] = user
            "User registered successfully!"
            cls.save_users()
            return True  # TODO make sure to add in running of programme, if true user registered

    # get users stored in the dict that have been retrieved from the file
    @classmethod
    def get_user(cls, username):
        return cls.users.get(username, None)  # none being the value returned if the username doesn't exist


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_new = True  # TODO do I need this, could be potentially useful for scalability but right now useless?

    def login(self):
        existing_user = UserManager.get_user(self.username)
        if existing_user and existing_user.password == self.password:
            "Login successful"
            return "login successful"
        else:
            return "login failed"  # TODO think about having a while loop at the stage of asking for the password in main.py

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
UserManager.retrieve_users()

# Testing if the login functionality works
username_1 = input("Please enter your username: ")  # use livvy.w23
password_1 = input("Please enter a password: ")  # user cheese

user_1 = User(username_1, password_1)

print(user_1.login())  # this should output login successful, however I keep getting login failed
# print(os.getcwd())
#
# response = UserManager.add_user(user_1)
#
# if response:
#     print("New user successfully registered")

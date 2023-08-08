# import getpass   NOT sure if I need this yet
import bcrypt


# initialise class for user management
class UserManager:
    users = {}  # dict to store the list of users, key for username, user object for value

    @classmethod
    def add_user(cls, user):
        if user.username in cls.users:
            "Username already exists"  # TODO if we didn't want a print inside function should this be in main? e.g if False
            return False
        else:
            cls.users[user.username] = user
            "User registered successfully!"
            return True

    @classmethod
    def get_user(cls, username):
        return cls.users.get(username, None)  # none being the value returned if the username doesn't exist


class User:
    def __init__(self, username, password):
        self.username = username
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.is_new = True

    def login(self, username):
        # if username[key] in self.users:
        existing_user = UserManager.get_user(self.username)
        if existing_user and existing_user.hashed_password == self.hashed_password:
            "Login successful"
            return True  # currently leave as boolean values as we may need it later to access menu, e.g. if true
        else:
            return False  # TODO think about having a while loop at the stage of asking for the password in main.py

    def change_password(self, password):
        # TODO add code here to change the user password?
        pass

    @staticmethod
    def logout(self):
        return "You have successfully been logged out"


class AdminUser(User):
    # will inherit all things from user class
    # need to return to this once we have created the admin section to see if more is needed
    pass


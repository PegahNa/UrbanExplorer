import unittest
import os
import json
from unittest import TestCase
from activity_recommender.auth.login import UserManager, User, ExistingUserError, UserValidationError


class TestAuthentication(TestCase):  # TODO check if I can do one class for both so it's one setup for both

    original_users_data = None
    dummy_data = None

    @classmethod
    def setUpClass(cls):
        # create a backup for original users data so tests do not intefere
        if os.path.exists(UserManager.user_file):
            with open(UserManager.user_file, "r") as file:
                cls.original_users_data = file.read()  # this will be re-instated in my file in the teardown
        else:
            cls.original_users_data = None

        # creating dummy data for testing:
        cls.dummy_data = {
                            "test1": {
                                "username": "test1",
                                "password": "pass1"
                            },
                            "test2": {
                                "username": "test2",
                                "password": "pass2"
                            },
                            "test3": {
                                "username": "test3",
                                "password": "pass3"
                            }
                        }

        # write dummy data into my JSON file
        with open(UserManager.user_file, "w") as file:
            json.dump(cls.dummy_data, file)

    def setUp(self):
        # Retrieve users before each test
        UserManager.retrieve_users()

    def test_retrieve_users(self):
        self.assertEqual(UserManager.users["test1"].username, "test1")
        self.assertEqual(UserManager.users["test1"].password, "pass1")

    def test_save_users(self):
        new_user = User("test4", "pass4")  # create new instance of user
        UserManager.users["test4"] = new_user  # add user to the class dict
        UserManager.save_users()

        # check if the user was saved correctly
        with open(UserManager.user_file, "r") as file:
            temp_data = json.load(file)
            # create message to print if test fails
            message = "The user is has not been saved into the file"
        self.assertIn("test4", temp_data, message)
        # TODO add something to test IO ERROR

    def test_add_user(self):
        new_user = User("test5", "pass5")
        UserManager.add_user(new_user)

        self.assertIn("test5", UserManager.users)
        with open(UserManager.user_file, 'r') as file:
            data = json.load(file)
        self.assertIn("test5", data)

    # test the right exceptions are raised
    def test_add_existing_user(self):
        existing_user = User("test1", "pass1")
        with self.assertRaises(ExistingUserError):
            UserManager.add_user(existing_user)

    def test_add_invalid_user(self):
        invalid_user = User("", "")
        with self.assertRaises(UserValidationError):
            UserManager.add_user(invalid_user)

    def test_get_user(self):
        user = UserManager.get_user("test1")
        self.assertEqual(user.username, "test1")
        self.assertEqual(user.password, "pass1")
        # TODO could add more testing to check None is passed when the user doesn't exist

    def test_valid_login(self):
        user = User("test1", "pass1")
        self.assertTrue(user.login())

    def test_invalid_login(self):
        user = User("test1", "notmypassword")
        self.assertFalse(user.login())

    def test_change_password(self):
        user = User("test1", "pass1")
        user.change_password("thisismynewpass")
        self.assertEqual(user.password, "thisismynewpass")

    def test_logout(self):
        self.assertEqual(User.logout(), "You have successfully been logged out")

    # initiate teardown so that we can restore original data post tests

    @classmethod
    def tearDownClass(cls):
        # Restore original data
        if cls.original_users_data:
            with open(UserManager.user_file, 'w') as file:
                file.write(cls.original_users_data)
        else:
            if os.path.exists(UserManager.user_file):
                os.remove(UserManager.user_file)


if __name__ == '__main__':
    unittest.main()

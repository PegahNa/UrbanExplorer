import unittest
import os
import json
from unittest import TestCase
from activity_recommender.auth.login import UserManager, User, ExistingUserError, UserValidationError, LoginError
from activity_recommender.utils.login_utils import verify_password, hash_password


class TestAuthentication(TestCase):
    original_users_data = None
    dummy_data = None
    @classmethod
    def setUpClass(cls):
        # create a backup for original users data so tests do not interfere
        if os.path.exists(UserManager.user_file):
            with open(UserManager.user_file, "r") as file:
                cls.original_users_data = file.read()  # this will be re-instated in my file in the teardown
        else:
            cls.original_users_data = None

        # creating dummy data for testing:
        # adding a hash function from utils to the dummy passwords
        cls.dummy_data = {
            "test1": {
                "username": "test1",
                "password": hash_password("pass1")
            },
            "test2": {
                "username": "test2",
                "password": hash_password("pass2")
            },
            "test3": {
                "username": "test3",
                "password": hash_password("pass3")
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
        # updated to reflect the hashed dummy data
        self.assertTrue(verify_password("pass1", UserManager.users["test1"].password))

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
        self.assertTrue(verify_password("pass5", UserManager.users["test5"].password))
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
        # updated to include hash verification
        self.assertTrue(verify_password("pass1", user.password))

    def test_valid_login(self):
        user = User("test1", "pass1")
        self.assertTrue(user.login())

    def test_invalid_login(self):
        user = User("test1", "notmypassword")
        with self.assertRaises(LoginError):
            user.login()

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

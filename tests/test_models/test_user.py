#!/usr/bin/python3
"""class TestUser"""


from models.user import User
import unittest
import models
import os


class TestUser(unittest.TestCase):
    """Represents a User"""

    def setUp(self):
        """SetUp method"""

        self.user = User()

    def TearDown(self):
        """TearDown method"""

        self.user = User()

    def test_docstring(self):
        """Tests docstring for module and class"""

        self.assertIsNotNone(
            models.user.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(User.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Tests permissions"""

        test_file = os.access("models/user.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/user.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/user.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Tests type object for User"""

        self.assertEqual(
            str(type(self.user)),
            "<class 'models.user.User'>")
        self.assertIsInstance(self.user, User)

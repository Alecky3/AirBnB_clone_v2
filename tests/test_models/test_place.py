#!/usr/bin/python3
"""class TestPlace"""


from models.place import Place
import unittest
import models
import os


class TestPlace(unittest.TestCase):
    """represents Place"""

    def setUp(self):
        """SetUp method"""

        self.place = Place()

    def tearDown(self):
        """tearDown method"""

        del self.place

    def test_doctsring(self):
        """Test docstring for module and class"""

        self.assertIsNotNone(
            models.place.__doc__,
            "No doctring in the module"
        )
        self.assertIsNotNone(Place.__doc__, "No doctring in the class")

    def test_permissions_file(self):

        test_file = os.access("models/place.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/place.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/place.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object for Place"""

        self.assertEqual(
            str(type(self.place)),
            "<class 'models.place.Place'>")
        self.assertIsInstance(self.place, Place)

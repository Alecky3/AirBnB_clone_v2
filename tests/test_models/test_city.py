#!/usr/bin/python3
"""class City"""


from models.city import City
import unittest
import models
import os


class TestCity(unittest.TestCase):
    """Represents City"""

    def setUp(self):
        """setUp method"""

        self.city = City()

    def tearDown(self):
        """tearDown method"""

        del self.city

    def test_docstring(self):
        """Test docstring for module and class"""

        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test permissions"""

        test_file = os.access("models/city.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/city.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/city,py", os.X_OK)
        #self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of City"""

        self.assertEqual(
            str(type(self.city)),
            "<class 'models.city.City'>")
        self.assertIsInstance(self.city, City)

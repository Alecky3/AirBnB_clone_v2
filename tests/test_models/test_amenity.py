#!/usr/bin/python3
"""class Amenity"""


from models.amenity import Amenity
import unittest
import models
import os


class TestAmenity(unittest.TestCase):
    """represents Amenity"""

    def setUp(self):
        """setUp method"""

        self.amenity = Amenity()

    def tearDown(self):
        """tearDown method"""

        del self.amenity

    def test_docstring(self):
        """Test docstring for module and the class"""

        self.assertIsNotNone(
            models.amenity.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Amenity.__doc__, "No docstring is the class")

    def test_permissions_file(self):
        """Test permissions"""

        test_file = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object"""

        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.amenity, Amenity)

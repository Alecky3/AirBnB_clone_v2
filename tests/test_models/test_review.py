#!/usr/bin/python3
"""class Review"""


from models.review import Review
import unittest
import models
import os


class TestReview(unittest.TestCase):
    """represents Review"""

    def setUp(self):
        """setUp method"""

        self.review = Review()

    def tearDowns(self):
        """tearDown method"""

        del self.review

    def test_docstring(self):
        """test docstring for module and class"""

        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the module")

    def test_permissions_file(self):
        """Test file for permissions"""

        test_file = os.access("models/review.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/review.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/review.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """test type object"""

        self.assertEqual(
            str(type(self.review)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(self.review, Review)

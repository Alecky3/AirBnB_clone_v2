#!/usr/bin/python3
"""class State"""


from models.state import State
import unittest
import models
import os


class TestState(unittest.TestCase):
    """represent State"""

    def setUp(self):
        """setUp method"""

        self.state = State()

    def tearDown(self):
        """tearDown method"""

        del self.state

    def test_docstring(self):
        """Test docstring for module and class"""

        self.assertIsNotNone(
            models.state.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(State.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """test file permissions"""

        test_file = os.access("models/state.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/state.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/state.py", os.X_OK)

    def test_type_object(self):
        """test type object"""

        self.assertEqual(
            str(type(self.state)),
            "<class 'models.state.State'>")
        self.assertIsInstance(self.state, State)

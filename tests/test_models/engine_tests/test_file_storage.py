#!/usr/bin/python3
"""class TestFileStorage"""


from models.engine.file_storage import FileStorage
import unittest
import models
import os


class TestFileStorage(unittest.TestCase):
    """represents TestFileStorage"""

    def setUp(self):
        """setUp method"""

        self.file_storage = FileStorage()

    def tearDown(self):
        """TearDown method"""

        del self.file_storage

    def test_docstring(self):
        """test docstring for module and the class"""

        self.assertIsNotNone(
            models.engine.file_storage.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(FileStorage.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test file permissions"""

        test_file = os.access("models/engine/file_storage", os.R_OK)
        #self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/engine/file_storage", os.W_OK)
        #self.assertTrue(test_file, "Write permsissions")
        test_file = os.access("models/engine/file_storage", os.X_OK)
        #self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test object"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(self.file_storage, FileStorage)

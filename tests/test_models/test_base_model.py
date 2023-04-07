#!/usr/bin/python3
"""Tests BaseModel."""


from models.base_model import BaseModel
import unittest
import models
import os


class TestBaseModel(unittest.TestCase):
    """represents TestBaseModel"""

    def setUp(self):
        """setUp method"""

        self.base_model = BaseModel()
        self.base_model.data = "Test data"

    def tearDown(self):
        """tearDown method"""

        del self.base_model

    def test_init_id(self):
        """Test different id per object created"""

        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, self.base_model.id)

    def test_copy_object(self):
        """Copy an object with kwargs init from BaseModel"""

        my_model_dict = self.base_model.to_dict()
        bm1 = BaseModel(**my_model_dict)
        self.assertEqual(bm1.id, self.base_model.id)

    def test_id_type(self):
        """Test the id type from BaseModel"""

        self.assertIsInstance(self.base_model.id, str)

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """test permissions"""

        test_file = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_mod_to_dict(self):
        """test dict representation in BaseModel"""

        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_type_object(self):
        """test type object"""

        self.assertEqual(
            str(type(self.base_model)),
            "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.base_model, BaseModel)

    def test_str_representation(self):
        """Test str representation of BaseModel"""

        str_rep = "[{:s}] ({:s}) {:s}".format(
            self.base_model.__class__.__name__,
            self.base_model.id,
            str(self.base_model.__dict__)
        )
        self.assertEqual(str_rep, str(self.base_model))

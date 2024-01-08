#!/usr/bin/python3
"""This is the ``test_base_model`` module
It contains tests for the BaseModel class
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines a class TestBaseModel to test BaseModel class"""

    #-----test for public instance attributes-----
    def test_id(self):
        """Tests all edge cases for the instance id"""
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_datetime(self):
        """Tests all edge cases for the datetime instances"""

        bm = BaseModel()

        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    #------test for public instance methods-------
    def test_save(self):
        """Tests all edge cases for the save methodo"""

        bm = BaseModel()

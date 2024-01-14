#!/usr/bin/env python3
"""This is the ``test_amenity`` module
It contains tests for the Amnity class"""

from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Defines a class TestAmenity to test Amenity class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.am1 = Amenity()
        self.am2 = Amenity()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.am1
        del self.am2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.am1, BaseModel)
        self.assertIsInstance(self.am2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.am1, Amenity)
        self.assertTrue(hasattr(self.am1, "id"))
        self.assertNotEqual(self.am1.id, self.am2.id)

    def test_init(self):
        """Test that instance of Amenity correctly created"""

        self.assertIs(type(self.am1), Amenity)
        self.assertEqual(self.am1.name, "")
        self.am1.name = "PUBG Mobile"

    
        attr_map = {
                    "id": str,
                    "name": str,
                    "created_at": datetime,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.am1.__dict__)
                self.assertIs(type(self.am1.__dict__[attr]), types)

        self.assertEqual(self.am1.name, "PUBG Mobile")

    def test_str_method(self):
        """testing the __str__ method, checking output"""

        string = "[Amenity] ({}) {}".format(self.am1.id, self.am1.__dict__)
        self.assertEqual(string, str(self.am1))

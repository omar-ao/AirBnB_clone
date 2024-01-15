#!/usr/bin/env python3
"""This is the ``test_city`` module
It contains tests for the City class"""

from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines a class TestState to test State class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.ct1 = City()
        self.ct2 = City()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.ct1
        del self.ct2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.ct1, BaseModel)
        self.assertIsInstance(self.ct2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.ct1, City)
        self.assertTrue(hasattr(self.ct1, "id"))
        self.assertNotEqual(self.ct1.id, self.ct2.id)

    def test_init(self):
        """Test that instance of City correctly created"""

        self.assertIs(type(self.ct1), City)
        self.assertEqual(self.ct1.name, "")
        self.ct1.name = "Toronto"
        self.assertEqual(self.ct1.state_id, "")
        self.ct1.state_id = "123-AB45-67890"

        attr_map = {
                    "id": str,
                    "name": str,
                    "created_at": datetime,
                    "state_id": str,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.ct1.__dict__)
                self.assertIs(type(self.ct1.__dict__[attr]), types)

        self.assertEqual(self.ct1.name, "Toronto")
        self.assertEqual(self.ct1.state_id, "123-AB45-67890")

    def test_str_method(self):
        """testing __str__ method, checking output"""

        string = "[City] ({}) {}".format(self.ct1.id, self.ct1.__dict__)
        self.assertEqual(string, str(self.ct1))

#!/usr/bin/env python3
"""This is the ``test_state`` module
It contains tests for the State class"""

from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines a class TestState to test State class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.st1 = State()
        self.st2 = State()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.st1
        del self.st2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.st1, BaseModel)
        self.assertIsInstance(self.st2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.st1, State)
        self.assertTrue(hasattr(self.st1, "id"))
        self.assertNotEqual(self.st1.id, self.st2.id)

    def test_init(self):
        """Test that instance of State correctly created"""

        self.assertIs(type(self.st1), State)
        self.assertEqual(self.st1.name, "")
        self.st1.name = "Ontario"

    
        attr_map = {
                    "id": str,
                    "name": str,
                    "created_at": datetime,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.st1.__dict__)
                self.assertIs(type(self.st1.__dict__[attr]), types)

        self.assertEqual(self.st1.name, "Ontario")

    def test_str_method(self):
        """testing __str__ method, checking output"""

        string = "[State] ({}) {}".format(self.st1.id, self.st1.__dict__)
        self.assertEqual(string, str(self.st1))

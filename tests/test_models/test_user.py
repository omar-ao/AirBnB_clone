#!/usr/bin/env python3
"""This is the ``test_user`` module
It contains tests for the User class"""

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Defines a class TestUser to test User class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.us1 = User()
        self.us2 = User()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.us1
        del self.us2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.us1, BaseModel)
        self.assertIsInstance(self.us2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.us1, User)
        self.assertTrue(hasattr(self.us1, "id"))
        self.assertNotEqual(self.us1.id, self.us2.id)

    def test_init(self):
        """Test that instance of User correctly created"""

        self.assertIs(type(self.us1), User)
        self.assertEqual(self.us1.email, "")
        self.us1.email = "mrsscott12@gmail.com"
        self.assertEqual(self.us1.password, "")
        self.us1.password = "{s1c2o3t4t&5&67890}"
        self.assertEqual(self.us1.first_name, "")
        self.us1.first_name = "Scott"
        self.assertEqual(self.us1.last_name, "")
        self.us1.last_name = "Richard"

        attr_map = {
                    "id": str,
                    "email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str,
                    "created_at": datetime,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.us1.__dict__)
                self.assertIs(type(self.us1.__dict__[attr]), types)

        self.assertEqual(self.us1.email, "mrsscott12@gmail.com")
        self.assertEqual(self.us1.password, "{s1c2o3t4t&5&67890}")
        self.assertEqual(self.us1.first_name, "Scott")
        self.assertEqual(self.us1.last_name, "Richard")

    def test_str_method(self):
        """testing __str__ method, checking output"""

        string = "[User] ({}) {}".format(self.us1.id, self.us1.__dict__)
        self.assertEqual(string, str(self.us1))

#!/usr/bin/env python3
"""This is the ``test_review`` module
It contains tests for the Review class"""

from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestState(unittest.TestCase):
    """Defines a class TestReview to test Review class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.rv1 = Review()
        self.rv2 = Review()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.rv1
        del self.rv2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.rv1, BaseModel)
        self.assertIsInstance(self.rv2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.rv1, Review)
        self.assertTrue(hasattr(self.rv1, "id"))
        self.assertNotEqual(self.rv1.id, self.rv2.id)

    def test_init(self):
        """Test that instance of State correctly created"""

        self.assertIs(type(self.rv1), Review)
        self.assertEqual(self.rv1.place_id, "")
        self.rv1.place_id = "NS.12345"
        self.assertEqual(self.rv1.user_id, "")
        self.rv1.user_id = "Scott.67890"
        self.assertEqual(self.rv1.text, "")
        self.rv1.text = "It's a wonderful location"

        attr_map = {
                    "id": str,
                    "place_id": str,
                    "user_id": str,
                    "text": str,
                    "created_at": datetime,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.rv1.__dict__)
                self.assertIs(type(self.rv1.__dict__[attr]), types)

        self.assertEqual(self.rv1.place_id, "NS.12345")
        self.assertEqual(self.rv1.user_id, "Scott.67890")
        self.assertEqual(self.rv1.text, "It's a wonderful location")

    def test_str_method(self):
        """testing __str__ method, checking output"""

        string = "[Review] ({}) {}".format(self.rv1.id, self.rv1.__dict__)
        self.assertEqual(string, str(self.rv1))

#!/usr/bin/env python3
"""This is the ``test_place`` module
It contains tests for the Place class"""

from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines a class TestPlace to test Place Class"""

    def setUp(self):
        """Setup all instances for the tests"""
        self.pc1 = Place()
        self.pc2 = Place()

    def tearDown(self):
        """TearDown all setUp instances after tests"""
        del self.pc1
        del self.pc2

    def test_is_subclass(self):
        """test for a subclass of BaseModel"""

        self.assertIsInstance(self.pc1, BaseModel)
        self.assertIsInstance(self.pc2, BaseModel)

    def test_id(self):
        """Tests all edge cases for the instance id"""

        self.assertIsInstance(self.pc1, Place)
        self.assertTrue(hasattr(self.pc1, "id"))
        self.assertNotEqual(self.pc1.id, self.pc2.id)

    def test_init(self):
        """Test that instance of Place correctly created"""

        self.assertIs(type(self.pc1), Place)
        self.assertEqual(self.pc1.city_id, "")
        self.pc1.city_id = "NV.12345"
        self.assertEqual(self.pc1.user_id, "")
        self.pc1.user_id = "Scott.67890"
        self.assertEqual(self.pc1.name, "")
        self.pc1.name = "The Cloud House"
        self.assertEqual(self.pc1.description, "")
        self.pc1.description = "A serene environment in the Hilmalayas"
        self.assertEqual(self.pc1.number_rooms, 0)
        self.pc1.number_rooms = 3
        self.assertEqual(self.pc1.number_bathrooms, 0)
        self.pc1.number_bathrooms = 2
        self.assertEqual(self.pc1.max_guest, 0)
        self.pc1.max_guest = 4
        self.assertEqual(self.pc1.price_by_night, 0)
        self.pc1.price_by_night = 50
        self.assertEqual(self.pc1.latitude, 0.0)
        self.pc1.latitude = 12.34
        self.assertEqual(self.pc1.longitude, 0.0)
        self.pc1.longitude = 56.78
        self.assertEqual(self.pc1.amenity_ids, [])
        self.pc1.amenity_ids = ["chess", "pool", "XBOX"]
    
        attr_map = {
                    "id": str,
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list,
                    "created_at": datetime,
                    "updated_at": datetime
                    }

        for attr, types in attr_map.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.pc1.__dict__)
                self.assertIs(type(self.pc1.__dict__[attr]), types)

        self.assertEqual(self.pc1.city_id, "NV.12345")
        self.assertEqual(self.pc1.user_id, "Scott.67890")
        self.assertEqual(self.pc1.name, "The Cloud House")
        self.assertEqual(self.pc1.description, "A serene environment in the Hilmalayas")
        self.assertEqual(self.pc1.number_rooms, 3)
        self.assertEqual(self.pc1.number_bathrooms, 2)
        self.assertEqual(self.pc1.max_guest, 4)
        self.assertEqual(self.pc1.price_by_night, 50)
        self.assertEqual(self.pc1.latitude, 12.34)
        self.assertEqual(self.pc1.longitude, 56.78)
        self.assertEqual(self.pc1.amenity_ids, ["chess", "pool", "XBOX"])

    def test_str_method(self):
        """testing __str__ method, checking output"""

        string = "[Place] ({}) {}".format(self.pc1.id, self.pc1.__dict__)
        self.assertEqual(string, str(self.pc1))

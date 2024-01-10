#!/usr/bin/python3
"""This is the ``test_file_storage`` module
It defines all tests for the class FileStorage
"""


import unittest
import json
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines a class TestFileStorage that defines tests
    for class FileStorage
    """

    #------------using test file instead of the actual file---------
    @patch("file_storage.FileStorage.__file_path", "test_file.json")

    def setUp(self):
        """Sets up all intances needed for the test methods"""
        self.storage = FileStorage()
        class TestObject:
            def __init__(self, id, name):
                self.id = id
                self.name = name
        test_obj = TestObject("12", "Python")

    def tearDown(self):
        """Clean up test file"""
        try:
            remove("test_file.json")
        except FileNotFoundError:
            pass

    #---------tests for public intance methods----------------
    def test_all(self):
        """Defines all test cases for the intance method all()"""
        result = self.storage.all()
        self.assertEqual(result, {})
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Defines all edge case tests for the method new()"""

        self.storage.new(test_obj)
        objects = self.storage.all()
        self.assertEqual(objects, {"TestObject.12": test_obj})
        with self.assertRaises(TypeError):
            self.storage.new()
            self.storage.new("Test", "Test")

    def test_save(self):
        """Defines all edge case tests for the method save()"""

        self.storage.new(test_obj)
        self.storage.save()

        with open("test_file.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data, {"TestObject.12": test_obj.__dict__})

    def test_reload(self):
        """Tests reload deserializes JSON file to objects"""

        with open("test_file.json", "w") as f:
            json.dump({"TestObject.12": test_obj.__dict__}, f)

        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(objects, {"TestObject.12": test_obj.__dict__}) 
        
    def test_reload_not_overwrites(self):
        """Tests reload does not overwrite existing objects"""

        obj1 = TestObject("13", "C is fun")
        self.storage.new(obj1)

        with open("test_file.json", "w") as f:
            json.dump({"TestObject.11": {"id": '11', "name": 'Python'}})

        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("TestObject.13", objects.keys())
        self.assertEqual(objects["TestObject.13"], obj1)

    def test_reald_missing_file(self):
        """Tests reload handles missing files"""

        try:
            remove("test_file.json")
        except FileNotFoundError:
            pass

        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

#!/usr/bin/python3
"""This module contains tests for
the console module
"""


from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
from unittest.mock import patch
import unittest
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    Tests for the class HBNBcommand
    """

    def setUp(self):
        """Set up all instances that will be used in the tests"""
        self.bm = BaseModel()
        
    def test_all_docs(self):
        """Tests all is documented"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertNotEqual(f.getvalue().strip(), "")

    def test_create_docs(self):
        """Tests create is documented"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertNotEqual(f.getvalue(), "")

    def test_all(self):
        """Test all prints all objects"""
        objects = storage.all()
        expected = [str(objects[k]) for k in objects.keys()]
        expected = str(expected) + "\n"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(expected, f.getvalue())

    def test_all_based_on_class_name(self):
        """
        Tests for all string representation of
        all instances based the class name
        """
        objects = storage.all()
        bm_objs = {k: v for k, v in objects.items() if "BaseModel" in k}
        expected = [str(bm_objs[k]) for k in bm_objs.keys()]
        expected = str(expected) + "\n"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(expected, f.getvalue())

    def test_all_non_existing_class(self):
        """
        Tests error for all with non existing class name
        """
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all blblb")
            self.assertEqual(expected, f.getvalue())

#!/usr/bin/python3
"""This module contains tests for
the console module
"""


from console import HBNBCommand
from io import StringIO
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from unittest.mock import patch
import cmd
import unittest


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
            HBNBCommand().onecmd("all abcd")
            self.assertEqual(expected, f.getvalue())

    def test_non_exist_command(self):
        """Test a command that doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("shazam")
            self.assertEqual('*** Unknown syntax: shazam\n' or '',
                             f.getvalue())

    def test_empty_line(self):
        """Test empty input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_help_quit(self):
        text = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_EOF(self):
        text = "Ctrl+D: Exits the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_create(self):
        text = ("Creates a new instance and saves it")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_show(self):
        text = ("Prints the string representation of an instance")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_update(self):
        text = ("Updates an instance based on the class name and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_destroy(self):
        text = ("Deletes an instances based on the class and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help_count(self):
        text = ("Retrieves the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(text, f.getvalue().strip())

    def test_help(self):
        text = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(text, f.getvalue().strip())

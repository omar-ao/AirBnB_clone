#!/usr/bin/python3
"""This is the ``file_storage`` module
It defines a class FileStorage that serializes instances
to JSON file and deserializes JSON fiel to instances
"""


class FileStorage:
    """Defines a class FileStorage that serializes instances
    to JSON file and deserializes JSON file to instances
    """

    def all(self):
        """Returns the dictionary objects"""

    def new(self, obj):
        """Sets in objects the obj with key <obj class name>.id

        Args:
            obj: Object that is set to the Objects dictionary
        """

    def save(self):
        """Serializes objects to the JSON file"""

    def reload(self):
        """Deserializes the JSON file to objects dictionary only if the
        JSON file exists
        """

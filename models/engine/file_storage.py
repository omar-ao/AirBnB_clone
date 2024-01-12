#!/usr/bin/python3
"""This is the ``file_storage`` module
It defines a class FileStorage that serializes instances
to JSON file and deserializes JSON fiel to instances
"""

import os
import json


class FileStorage:
    """Defines a class FileStorage that serializes instances
    to JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in objects the obj with key <obj class name>.id

        Args:
            obj: Object that is set to the Objects dictionary
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""

        obj_cp = {}
        for keys in self.__objects:
            obj_cp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_cp, f)

    def reload(self):
        """Deserializes the JSON file to objects dictionary only if the
        JSON file exists
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dict_obj = {}
        cls_mapping = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)

            for key, value in json_dict.items():
                cls_name, obj_id = key.split(".")
                dict_obj[key] = cls_mapping[cls_name](**value)

            self.__objects = dict_obj
        except FileNotFoundError:
            pass

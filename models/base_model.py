#!/usr/bin/python3
"""This is the ``base_model`` module
It defines one class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines a class BaseModel"""
    
    def __init__(self):
        """Initializes the instance based on id, date created and date updated
        id is universilly unique identifier for each instances
        """
        
    def __str__(self):
        """Prints the instances int this format
        [<class name>] (<self.id>) <self.__dict__>
        """

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """

    def to_dict(self):
        """Returns dictionary containing all keys/value the instance"""

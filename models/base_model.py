#!/usr/bin/python3
"""This is the ``base_model`` module
It defines one class BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines a class BaseModel"""
    
    def __init__(self, *args, **kwargs):
        """Initializes the instance based on id, date created and date updated
        id is universilly unique identifier for each instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)
        
    def __str__(self):
        """Prints the instances int this format
        [<class name>] (<self.id>) <self.__dict__>
        """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/value the instance
        (json serialization)
        """

        json = {k: v for k, v in self.__dict__.items()}
        json['__class__'] = self.__class__.__name__
        json['created_at'] = json['created_at'].isoformat()
        json['updated_at'] = json['updated_at'].isoformat()
        
        return json

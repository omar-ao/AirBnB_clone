#!/usr/bin/python3
"""This module contains one class Amenity"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines a class amenity that is on BaseModel

    Attributes:
        name(str): Amenity name
    """

    name = ""

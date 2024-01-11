#!/usr/bin/python3
"""This module contains one class, Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a class Review based on BaseModel

    Attributes:
        place_id(str): The id of the place reviewed
        user_id(str): The id of the user reviewing
        text(str): User's review text
    """

    place_id = ""
    user_id = ""
    text = ""

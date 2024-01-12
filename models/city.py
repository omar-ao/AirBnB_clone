#!/usr/bin/python3
"""This module defines class city"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines a class city that inherits
    from base model

    Attributes:
        state_id(str): State id
        name(str): City name
    """

    state_id = ""
    name = ""

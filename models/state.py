#!/usr/bin/python3
"""This module defines class state"""


from models.base_model import BaseModel


class State(BaseModel):
    """Defines a class state that
    inherits from basemodel

    Attributes:
        name(str): State name
    """

    name = ""

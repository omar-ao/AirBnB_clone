#!/usr/bin/python3
"""The User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class User that inherits from BaseModel

    Attributes:
        email(string): Users email
        password(string): Users password
        first_name(string): Users First name
        last_name(string): Users Last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

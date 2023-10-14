#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from base_model import BaseModel


class User(BaseModel):
    """ Represents a User

    Attributes:
        email (str): The user's email
        password (str): The user's password
        first_name (str): The user's firstname
        last_name (str): The user's lastname
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

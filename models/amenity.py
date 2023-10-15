#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from models.base_model import BaseModel


class User(BaseModel):
    """ Represents an Amenity

    Attributes:
        name (str): The Amenity's name
    """

    name = ""

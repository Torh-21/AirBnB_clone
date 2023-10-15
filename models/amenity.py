#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents an Amenity

    Attributes:
        name (str): The Amenity's name
    """

    name = ""

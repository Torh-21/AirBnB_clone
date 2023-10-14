#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from base_model import BaseModel


class User(BaseModel):
    """ Represents a Review

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    test = ""

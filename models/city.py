#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from base_model import BaseModel
from state import State

class User(BaseModel):
    """ Represents a City

    Attributes:
        state_id (str): It will be the State.id
        name (str): The city name
    """

    state_id = ""
    name = ""

#!/usr/bin/env python3
""" This class inherits from the "BaseModel" class """

from models.base_model import BaseModel


class State(BaseModel):
    """ Represents a State

    Attributes:
        name (str): The state's name
    """

    name = ""

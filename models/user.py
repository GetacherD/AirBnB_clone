#!/usr/bin/python3
"""
user Module
"""
from models.base_model import BaseModel


class User(BaseModel):

    """ User Representation """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

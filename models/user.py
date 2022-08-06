#!/usr/bin/python3
"""
user Module
"""
from models.base_model import BaseModel


class User(BaseModel):

    """ User Representation """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

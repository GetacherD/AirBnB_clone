#!/usr/bin/python3
"""
Base Model to be inherited
"""
import uuid
from datetime import datetime


class BaseModel:

    """ Base Model Representation """
    def __init__(self, *args, **kwargs):

        """ Initialization with or with out kwargs
        kwargs assumed to contain isoformatted datetime object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):

        """ String Representation """
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):

        """ save instance to file"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):

        """ Return Dict Representation """
        dic = self.__dict__.copy()
        dic["updated_at"] = dic["updated_at"].isoformat()
        dic["created_at"] = dic["created_at"].isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

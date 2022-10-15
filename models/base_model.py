#!/usr/bin/python3
"""
Base Model to be inherited
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ Base Model for all """
    def __init__(self, *args, **kwargs):
        """ Initialize new object """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """ str representation """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ save instance """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ convert to dict """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["updated_at"] = datetime.isoformat(res["updated_at"])
        res["created_at"] = datetime.isoformat(res["created_at"])
        return res

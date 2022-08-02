#!/usr/bin/python3
"""
Base Model to be inherited
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """ Base Model Representation """
    def __init__(self, *args, **kwargs):

        """ Initialization """
        if kwargs is None or kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):

        """ String Representation """
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       getattr(self, "id"), self.__dict__)

    def save(self):

        """ save instance to file"""
        setattr(self, "updated_at",  datetime.now())
        storage.save()

    def to_dict(self):

        """ Return Dict Representation """
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic

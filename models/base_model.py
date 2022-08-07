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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        try:
                            setattr(self, key, datetime.fromisoformat(value))
                        except (TypeError, ValueError):
                            setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):

        """ String Representation """
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       getattr(self, "id"), self.__dict__)

    def save(self):

        """ save instance to file"""
        setattr(self, "updated_at",  datetime.now())
        storage.new(self)
        storage.save()

    def to_dict(self):

        """ Return Dict Representation """
        dic = {}
        for key, value in self.__dict__.items():
            if key in ["updated_at", "created_at"]:
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        dic["__class__"] = self.__class__.__name__
        return dic

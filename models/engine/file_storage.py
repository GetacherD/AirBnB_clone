#!/usr/bin/python3
"""
File Storage Module
"""
import os
import json
from json import JSONEncoder
from datetime import datetime
from os.path import exists
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place


class DateTimeEncoder(JSONEncoder):

    """ DateTimeEncoder to encode datetime objecsts to json"""
    def default(self, o):

        """ Default encoding """
        if isinstance(o, (datetime, datetime.date)):
            return o.isoformat()
        return super().default(o)


'''
class DateTimeDecoder(JSONDecoder):

    """ Custom DateTimeDecoder """
    def __init__(self, **kwargs):
        kwargs.setdefault("object_hook", self.object_hook)
        super().__init__(**kwargs)

    def object_hook(self, dict_):
        """Try to decode a complex number."""
        dic = {}
        for key, value in dict_.items():
            try:
                dic[key] = datetime.fromisoformat(value)
            except (ValueError, TypeError, json.decoder.JSONDecodeError):
                dic[key] = value
        return dic

'''


class FileStorage:

    """ File Storage Objects Representation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """ Return all objecsts """
        return FileStorage.__objects

    def new(self, obj):

        """ add new object to dictionary of objecsts"""
        FileStorage.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):

        """ save objects dictionary to json file"""
        data = FileStorage.__objects.copy()
        mydic = {}
        for key, obj in data.items():
            mydic[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(mydic, f)

    def reload(self):

        """ Deserialize, load objects from json"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                FileStorage.__objects = {}
                for key, value in data.items():
                    obj = eval(key.split(".")[0])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return

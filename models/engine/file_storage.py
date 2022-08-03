#!/usr/bin/python3
"""
File Storage Module
"""
import json
from json import JSONEncoder
from datetime import datetime
from os.path import exists


class DateTimeEncoder(JSONEncoder):

    """ DateTimeEncoder to encode datetime objecsts to json"""
    def default(self, o):

        """ Default encoding """
        if isinstance(o, (datetime, datetime.date)):
            return o.isoformat()
        return super().default(o)


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
            "{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):

        """ save objects dictionary to json file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects, cls=DateTimeEncoder))

    def reload(self):

        """ Deserialize, load objects from json"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                result = f.read()
                if result:
                    FileStorage.__objects = json.loads(result)

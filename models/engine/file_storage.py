#!/usr/bin/python3
"""
File Storage Module
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """ File storage representation"""
    __file_path = "file.json"
    """ Store all objects as key:value(object)"""
    __objects = {}

    def all(self):
        """ Retrive all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ add new object to __objects dict """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save __objects dict to file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dump = {}
            for key, value in FileStorage.__objects.items():
                dt = {}
                for k, v in value.to_dict().items():
                    dt[k] = v
                dump[key] = dt
            file.write(json.dumps(dump))

    def reload(self):
        """ reload from file all objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.loads(file.read())
                for key, value in data.items():
                    dt = {}
                    for k, v in value.items():
                        dt[k] = v
                    obj = eval("{}".format(key.split(".")[0]))(**dt)
                    self.new(obj)
        except FileNotFoundError:
            return

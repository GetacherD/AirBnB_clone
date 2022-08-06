#!/usr/bin/python3
"""
Test For base_model
"""
import unittest
import datetime
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()


def setUpModule():
    print("Test BaseModel\n")


def tearDownModule():
    print("\nEnd of test BaseModel")


class TestBaseModel(unittest.TestCase):

    """ Test for BaseModel"""
    @classmethod
    def setUpClass(cls):
        os.system("touch ./file.json")

    def test_uniq_id(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_updated_at(self):
        obj = BaseModel()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test__str__(self):

        obj = BaseModel()
        obj_str = obj.__str__()
        self.assertTrue("BaseModel" in obj_str and
                        "id" in obj_str and "created_at" in obj_str and
                        "updated_at" in obj_str)

    def test_save(self):

        obj = BaseModel()
        obj.save()
        with open("file.json", encoding="utf-8") as f:
            data = f.read()
            self.assertTrue("updated_at" in data)

    def test_to_dict__class__key(self):

        obj = BaseModel()
        self.assertTrue("__class__" in obj.to_dict())

    def test_to_dict__iso_format(self):

        obj = BaseModel()
        dic = obj.to_dict()
        created_at = dic.get("created_at")
        self.assertTrue("datetime" not in created_at)

    def test_empty_object(self):

        obj = BaseModel()
        _id = str(obj.id)
        objects = storage.all()
        self.assertTrue(f"BaseModel.{_id}" in objects)

    def test_create_with_kwargs(self):

        """ Test create empty obj, save it, create another obj1
        from obj1 compare their id"""
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel(**{"id": obj1.id,
                            "created_at": obj1.created_at,
                            "updated_at": obj1.updated_at,
                            "Name": "Bety", "Age": 4})
        self.assertEqual(obj2.to_dict().get("id"), obj1.id)
        with open('file.json', encoding="utf-8") as f:
            data = json.loads(f.read())
            d = data.get(f"BaseModel.{obj1.id}")
            obj3 = BaseModel(**d)
            self.assertEqual(obj3.id, obj1.id)

    @classmethod
    def tearDownClass(cls):

        os.system("rm ./file.json")

#!/usr/bin/python3
"""
Test For User
"""
import unittest
import datetime
from unittest.mock import patch
import os
import json
from io import StringIO
from models.engine.file_storage import FileStorage
from models.user import User
storage = FileStorage()


def setUpModule():
    """Run before all test"""
    print("Test User\n")


def tearDownModule():
    """Run after all test"""
    print("\nEnd of test User")


class TestUser(unittest.TestCase):
    """ Test for User"""

    @classmethod
    def setUpClass(cls):
        """Create an empty file.json"""
        os.system("touch ./file.json")

    def test_email(self):

        """ test for email"""
        u = User()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.email)
            self.assertEqual("\n", stdout.getvalue())

    def test_password(self):

        """ test for email"""
        u = User()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.password)
            self.assertEqual("\n", stdout.getvalue())

    def test_first_name(self):

        """ test for email"""
        u = User()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.first_name)
            self.assertEqual("\n", stdout.getvalue())

    def test_last_name(self):

        """ test for email"""
        u = User()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.last_name)
            self.assertEqual("\n", stdout.getvalue())

    def test_uniq_id(self):
        """Remove file.json after all test"""

        obj1 = User()
        obj2 = User()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_updated_at(self):
        """Testing new object will be updated"""

        obj = User()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test__str__(self):
        """Testing the string represantation"""

        obj = User()
        obj_str = obj.__str__()
        self.assertTrue("User" in obj_str and
                        "id" in obj_str and "created_at" in obj_str and
                        "updated_at" in obj_str)

    def test_save(self):
        """Testing the save method work or not"""

        obj = User()
        obj.save()
        with open("file.json", encoding="utf-8") as f:
            data = f.read()
            self.assertTrue("updated_at" in data)

    def test_to_dict__class__key(self):
        """Testing dictionary class and key"""

        obj = User()
        self.assertTrue("__class__" in obj.to_dict())

    def test_to_dict__iso_format(self):
        """Testing dictionary holds iso format or not"""

        obj = User()
        dic = obj.to_dict()
        created_at = dic.get("created_at")
        self.assertTrue("datetime" not in created_at)

    def test_empty_object(self):
        """Testing the object empty or not"""

        obj = User()
        _id = str(obj.id)
        objects = storage.all()
        self.assertTrue(f"User.{_id}" in objects)

    def test_create_with_kwargs(self):
        """ Test create empty obj, save it, create another obj1
        from obj1 compare their id"""

        obj1 = User()
        obj1.save()
        obj2 = User(**{"id": obj1.id,
                       "created_at": obj1.created_at.isoformat(),
                       "updated_at": obj1.updated_at.isoformat(),
                       "Name": "Bety", "Age": 4})
        self.assertEqual(obj2.to_dict().get("id"), obj1.id)
        with open('file.json', encoding="utf-8") as f:
            data = json.loads(f.read())
            d = data.get(f"User.{obj1.id}")
            obj3 = User(**d)
            self.assertEqual(obj3.id, obj1.id)

    @classmethod
    def tearDownClass(cls):
        """Remove a class after all test"""

        os.system("rm ./file.json")

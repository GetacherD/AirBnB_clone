#!/usr/bin/python3
"""
Test For Review
"""
import unittest
import datetime
import os
import json
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.review import Review
storage = FileStorage()


def setUpModule():
    """Run before all test"""
    print("Test Review\n")


def tearDownModule():
    """Run after all test"""
    print("\nEnd of test Review")


class TestReview(unittest.TestCase):
    """ Test for Review"""

    @classmethod
    def setUpClass(cls):
        """Create an empty file.json"""
        os.system("touch ./file.json")

    def test_place_id(self):

        """ test for email"""
        u = Review()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.place_id)
            self.assertEqual("\n", stdout.getvalue())

    def test_user_id(self):

        """ test for email"""
        u = Review()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.user_id)
            self.assertEqual("\n", stdout.getvalue())

    def test_text(self):

        """ test for email"""
        u = Review()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.text)
            self.assertEqual("\n", stdout.getvalue())

    def test_uniq_id(self):
        """Remove file.json after all test"""

        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_updated_at(self):
        """Testing new object will be updated"""

        obj = Review()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test__str__(self):
        """Testing the string represantation"""

        obj = Review()
        obj_str = obj.__str__()
        self.assertTrue("Review" in obj_str and
                        "id" in obj_str and "created_at" in obj_str and
                        "updated_at" in obj_str)

    def test_save(self):
        """Testing the save method work or not"""

        obj = Review()
        obj.save()
        with open("file.json", encoding="utf-8") as f:
            data = f.read()
            self.assertTrue("updated_at" in data)

    def test_to_dict__class__key(self):
        """Testing dictionary class and key"""

        obj = Review()
        self.assertTrue("__class__" in obj.to_dict())

    def test_to_dict__iso_format(self):
        """Testing dictionary holds iso format or not"""

        obj = Review()
        dic = obj.to_dict()
        created_at = dic.get("created_at")
        self.assertTrue("datetime" not in created_at)

    def test_empty_object(self):
        """Testing the object empty or not"""

        obj = Review()
        _id = str(obj.id)
        objects = storage.all()
        self.assertTrue(f"Review.{_id}" in objects)

    def test_create_with_kwargs(self):
        """ Test create empty obj, save it, create another obj1
        from obj1 compare their id"""

        obj1 = Review()
        obj1.save()
        obj2 = Review(**{"id": obj1.id,
                         "created_at": obj1.created_at.isoformat(),
                         "updated_at": obj1.updated_at.isoformat(),
                         "Name": "Bety", "Age": 4})
        self.assertEqual(obj2.to_dict().get("id"), obj1.id)
        with open('file.json', encoding="utf-8") as f:
            data = json.loads(f.read())
            d = data.get(f"Review.{obj1.id}")
            obj3 = Review(**d)
            self.assertEqual(obj3.id, obj1.id)

    @classmethod
    def tearDownClass(cls):
        """Remove a class after all test"""

        os.system("rm ./file.json")

#!/usr/bin/python3
"""
Test For Place
"""
import unittest
import datetime
import os
import json
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.place import Place
storage = FileStorage()


def setUpModule():
    """Run before all test"""
    print("Test Place\n")


def tearDownModule():
    """Run after all test"""
    print("\nEnd of test Place")


class TestPlace(unittest.TestCase):
    """ Test for Place"""

    @classmethod
    def setUpClass(cls):
        """Create an empty file.json"""
        os.system("touch ./file.json")

    def test_city_id(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.city_id)
            self.assertEqual("\n", stdout.getvalue())

    def test_user_id(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.user_id)
            self.assertEqual("\n", stdout.getvalue())

    def test_name(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.name)
            self.assertEqual("\n", stdout.getvalue())

    def test_description(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.description)
            self.assertEqual("\n", stdout.getvalue())

    def test_number_rooms(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.number_rooms)
            self.assertEqual("0\n", stdout.getvalue())

    def test_number_bathrooms(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.number_bathrooms)
            self.assertEqual("0\n", stdout.getvalue())

    def test_max_guest(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.max_guest)
            self.assertEqual("0\n", stdout.getvalue())

    def test_price_by_night(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.price_by_night)
            self.assertEqual("0\n", stdout.getvalue())

    def test_latitude(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.latitude)
            self.assertEqual("0.0\n", stdout.getvalue())

    def test_longitude(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.longitude)
            self.assertEqual("0.0\n", stdout.getvalue())

    def test_amenity_id(self):

        """ test for email"""
        u = Place()
        with patch("sys.stdout", new=StringIO()) as stdout:
            print(u.amenity_ids)
            self.assertEqual("[]\n", stdout.getvalue())

    def test_uniq_id(self):
        """Remove file.json after all test"""

        obj1 = Place()
        obj2 = Place()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_updated_at(self):
        """Testing new object will be updated"""

        obj = Place()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test__str__(self):
        """Testing the string represantation"""

        obj = Place()
        obj_str = obj.__str__()
        self.assertTrue("Place" in obj_str and
                        "id" in obj_str and "created_at" in obj_str and
                        "updated_at" in obj_str)

    def test_save(self):
        """Testing the save method work or not"""

        obj = Place()
        obj.save()
        with open("file.json", encoding="utf-8") as f:
            data = f.read()
            self.assertTrue("updated_at" in data)

    def test_to_dict__class__key(self):
        """Testing dictionary class and key"""

        obj = Place()
        self.assertTrue("__class__" in obj.to_dict())

    def test_to_dict__iso_format(self):
        """Testing dictionary holds iso format or not"""

        obj = Place()
        dic = obj.to_dict()
        created_at = dic.get("created_at")
        self.assertTrue("datetime" not in created_at)

    def test_empty_object(self):
        """Testing the object empty or not"""

        obj = Place()
        _id = str(obj.id)
        objects = storage.all()
        self.assertTrue(f"Place.{_id}" in objects)

    def test_create_with_kwargs(self):
        """ Test create empty obj, save it, create another obj1
        from obj1 compare their id"""

        obj1 = Place()
        obj1.save()
        obj2 = Place(**{"id": obj1.id,
                        "created_at": obj1.created_at.isoformat(),
                        "updated_at": obj1.updated_at.isoformat(),
                        "Name": "Bety", "Age": 4})
        self.assertEqual(obj2.to_dict().get("id"), obj1.id)
        with open('file.json', encoding="utf-8") as f:
            data = json.loads(f.read())
            d = data.get(f"Place.{obj1.id}")
            obj3 = Place(**d)
            self.assertEqual(obj3.id, obj1.id)

    @classmethod
    def tearDownClass(cls):
        """Remove a class after all test"""

        os.system("rm ./file.json")

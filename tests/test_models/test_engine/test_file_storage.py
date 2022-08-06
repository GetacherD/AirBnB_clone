#!/usr/bin/python3
"""
Test File Storage
"""
import unittest
import os
import json
from os.path import exists
from models.user import User
from models.engine.file_storage import FileStorage
from models.engine.file_storage import DateTimeDecoder
from models.engine.file_storage import DateTimeEncoder
storage = FileStorage()

storage.reload()


def setUpModule():
    """Print before all test"""
    print("Testing FileStorage\n")


def tearDownModule():
    """print after all test"""
    print("\nEnd  of Testing FileStorage")


class TestFileStorage(unittest.TestCase):
    """Testing the file storage function"""

    @classmethod
    def setUpClass(cls):
        """Create a file befor all test file run"""
        os.system("touch file.json")

    @classmethod
    def tearDownClass(cls):
        """Create a file befor all test file run"""

        os.system("rm -r file.json")

    def test_all(self):
        """Create a file befor all test file run"""

        obj1 = User()
        _id1 = obj1.id
        obj1.save()
        obj2 = User()
        _id2 = obj2.id
        obj2.save()
        obj3 = User()
        _id3 = obj3.id
        obj3.save()
        with open("file.json", encoding="utf-8") as f:
            data = json.loads(f.read(), cls=DateTimeDecoder)
            ids = [f"User.{_id1}", f"User.{_id2}", f"User.{_id3}"]
            exp = True
            for key in ids:
                if key not in data:
                    exp = False
            self.assertTrue(exp)

    def test_new(self):
        """Create a file befor all test file run"""

        obj = User()
        key = f"User.{obj.id}"
        objects = json.dumps(storage.all(), cls=DateTimeEncoder)
        self.assertTrue(key in objects)

    def test_save(self):
        """Create a file befor all test file run"""

        os.system("touch file.json")
        os.system("rm file.json")
        self.assertFalse(exists("file.json"))
        obj = User()
        self.assertFalse(exists("file.json"))
        obj.save()
        self.assertTrue(exists("file.json"))
        key = f"User.{obj.id}"
        objects = storage.all()
        self.assertTrue(key in objects)

    def test_reload_empty_file(self):
        """Create a file befor all test file run"""

        os.system("touch file.json")
        os.system("rm file.json")
        os.system("touch file.json")
        storage.reload()
        objects = storage.all()
        self.assertEqual({}, objects)

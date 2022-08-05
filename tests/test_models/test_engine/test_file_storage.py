#!/usr/bin/python3
"""
Test File Storage
"""
from io import StringIO
from unittest.mock import patch
from datetime import datetime
import unittest
import os
import json
from models.user import User
from models.engine.file_storage import FileStorage
from models.engine.file_storage import DateTimeDecoder
from models.engine.file_storage import DateTimeEncoder
storage = FileStorage()

storage.reload()


class TestFileStorage(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        os.system("touch file.json")
    @classmethod
    def tearDownClass(cls):
        os.system("rm -r file.json")

    def test_all(self):

        obj1 = User()
        obj1.save()
        obj2 = User()
        obj2.save()
        obj3 = User()
        obj3.save()
        with open("file.json") as f:
            data = json.loads(f.read(), cls=DateTimeDecoder)
            count = 0
            for key in data:
                count += 1
            self.assertEqual(3, count)

    def test_new(self):

        obj = User()
        key = f"User.{obj.id}"
        objects = json.dumps(storage.all(), cls=DateTimeEncoder)
        self.assertTrue(key in objects)
        

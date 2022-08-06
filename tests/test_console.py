#!/usr/bin/python3
"""
Testing The Console
"""
from io import StringIO
from unittest.mock import patch
import unittest
import json
import os
from console import HBNBCommand
from models import storage
from models.engine.file_storage import DateTimeEncoder
from models.user import User


def setUpModule():
    print("Testing Console")


def tearDownModule():
    print("\nEnd of Test Console")


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system("touch file.json")

    @classmethod
    def tearDownClass(cls):
        """ Test Console """
        os.system("rm -f file.json")

    def test_create_ok(self):

        """ Testing Console create command """
        with patch('sys.stdout', new=StringIO()) as stdout:
            HBNBCommand().onecmd("create Place")
            _id = str(stdout.getvalue())[:-1]
            key = f"Place.{_id}"
            objects = storage.all()
            self.assertTrue(key in objects)

    def test_create_class_not_exist(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("create NOCLASS")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_create_name_missing(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("create")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_show_ok(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            obj = User()
            obj.save()
            HBNBCommand().onecmd(f"show User {obj.id}")
            data = str(stdout.getvalue())
            self.assertTrue(f"{obj.id}" in data)

    def test_show_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("show Plac")
            exp = "** class doesn't exist **\n"
            self.assertTrue(exp, stdout.getvalue())

    def test_show_class_missing(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("show")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_show_id_missing(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("show BaseModel")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_show_id_instance_not_found(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("show BaseModel 0.5")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_destroy_ok(self):
        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"destroy User {obj.id}")
            HBNBCommand().onecmd("all")
            data = str(stdout.getvalue())
            self.assertTrue(str(obj.id) not in data)

    def test_destroy_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("destroy")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_destroy_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("destroy Base")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_destroy_id_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("destroy User")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_destroy_id_instance_not_found(self):
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("destroy User 0.4")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_all_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("all class")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_all_user(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("all User")
            lst = json.dumps(stdout.getvalue())
            exp = True
            for item in ["BaseModel", "Place", "City", "Review", "Amenity"]:
                if item in lst:
                    exp = False
            self.assertTrue(exp)

    def test_all(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("all")
            lst = json.dumps(stdout.getvalue(), cls=DateTimeEncoder)
            checks = ["datetime.datetime", "__class__",
                      "created_at", "updated_at", "id", "(", ")", "[", "]"]
            exp = True
            for item in checks:
                if item not in lst:
                    exp = False
            if '[' in lst and ']' in lst:
                exp = True
            self.assertTrue(exp)

    def test_update_ok(self):

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"update User {obj.id} __attrib__  __Value__")
            HBNBCommand().onecmd(f"show User {obj.id}")
            data = str(stdout.getvalue())
            self.assertTrue("__attrib__" in data and "__Value__" in data)

    def test_update_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("update")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_update_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("update myModel")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_update_id_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("update User")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_update_id_instance_not_found(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("update User 0.8")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_update_attr_missing(self):

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"update User {obj.id}")
            exp = "** attribute name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_update_attr_value_missing(self):

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"update User {obj.id} Name")
            exp = "** value missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_model_dot_all(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.all()")
            lst = json.dumps(stdout.getvalue())
            exp = True
            for item in ["BaseModel", "Place", "City", "Review", "Amenity"]:
                if item in lst:
                    exp = False
            self.assertTrue(exp)

    def test_model_dot_count(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.count()")
            exp = int(stdout.getvalue()) >= 0
            self.assertTrue(exp)

    def test_model_dot_count_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("U.count()")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_model_dot_count_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(".count()")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_model_dot_all_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(".all()")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_model_dot_all_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("U.all()")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_show_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(".show('1212')")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_show_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("a.show(12112)")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_show_id_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.show()")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_show_id_instance_not_found(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.show('0.7')")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_destroy_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(".destroy('1212')")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_destroy_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("a.destroy(12112)")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_destroy_id_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.destroy()")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_destroy_id_instance_not_found(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.destroy('0.7')")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_class_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(".update('1212')")
            exp = "** class name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_class_not_exist(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("a.update(12112)")
            exp = "** class doesn't exist **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_id_missing(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.update()")
            exp = "** instance id missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_id_instance_not_found(self):

        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd("User.update('0.7')")
            exp = "** no instance found **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_attr_missing(self):

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"User.update({obj.id})")
            exp = "** attribute name missing **\n"
            self.assertEqual(exp, stdout.getvalue())

    def test_dot_update_attr_value_missing(self):

        obj = User()
        obj.save()
        with patch("sys.stdout", new=StringIO()) as stdout:
            HBNBCommand().onecmd(f"User.update({obj.id}, Name)")
            exp = "** value missing **\n"
            self.assertEqual(exp, stdout.getvalue())

#!/usr/bin/python3
"""
Console
"""
import cmd
import sys
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):

    """ command line interface"""
    prompt = "(hbnb)"
    __classes = {"BaseModel": BaseModel, "State": State,
                 "Place": Place, "Review": Review,
                 "Amenity": Amenity, "User": User, "City": City}

    def do_quit(self, args):

        """ enter quit to Exit program"""
        try:
            sys.exit(int(args))
        except (ValueError, TypeError):
            sys.exit(0)

    def help_quit(self):
        print("Enter Quit to Exit program")

    def do_EOF(self, args):

        """ Exit program on CTRL+D"""
        print(args)
        sys.exit(-1)

    def help_EOF(self):
        print("Exit Program on CTRL+D")

    def do_create(self, args):

        """ Create New Object of BaseModel
            Syntax: create [ModelName]"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_object = HBNBCommand.__classes[args]()
            new_object.save()
            print(new_object.id)

    def help_create(self):
        print("Create New Object of BaseModel")
        print("[Syntax:] Create [ModelName]")

    def do_show(self, args):

        """ Print instance of object of given id
         Syntax: show [ModelName] [id]"""
        if not args:
            print("** class name missing **")
        elif args.split(" ")[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            class_name = args.split(" ")[0]
            _id = args.split(" ")[-1]
            obj = objects.get(f"{class_name}.{_id}", "* no instance found **")
            print(obj)

    def help_show(self):
        print("Print Instance of Object of given Id")
        print("[Syntax:] show [ModelName] [Id]")

    def do_destroy(self, args):

        """ Destroy an object \n Syntax: destroy [ModelName] [id]"""
        if not args:
            print("** class name missing **")
        elif args.split(" ")[0] not in HBNBCommand.__classes:
            print("** class doesn't exist ** ")
        elif len(args.split(" ")) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            class_name = args.split(" ")[0]
            _id = args.split(" ")[-1]
            obj = objects.get(f"{class_name}.{_id}", "* no instance found **")
            if obj != "* no instance found **":
                del objects[f"{class_name}.{_id}"]
            else:
                print("** no instance found **")
            storage.save()

    def help_destroy(self):
        print("Destroy an object")
        print("[Syntax:] destroy [ModelName] [id]")

    def do_all(self, args):

        """ Print all objects
            Syntax: all [ModelName] (optional)"""
        if args and args in HBNBCommand.__classes:
            objects = storage.all()
            obj_list = []
            for key, value in objects.items():
                obj = {}
                if key.split(".")[0] == args.split(" ")[0]:
                    for k, val in value.items():
                        try:
                            obj[k] = datetime.fromisoformat(val)
                        except ValueError:
                            obj[k] = val
                    obj_list.append(
                        f"[{key.split('.')[0]}] ({key.split('.')[1]}) {obj}")
            print(obj_list)
        elif args and args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            obj_list = []
            for key, value in objects.items():
                obj = {}
                for k, val in value.items():
                    try:
                        obj[k] = datetime.fromisoformat(val)
                    except ValueError:
                        obj[k] = val
                obj_list.append(
                    f"[{key.split('.')[0]}] ({key.split('.')[1]}) {obj}"
                )
            print(obj_list)

    def help_all(self):
        print("Print all objects")
        print("[Syntax:] all [ModelName] (optional)")

    def do_update(self, args):

        """ update /add attribute
            Syntax: update [ModelName] [id] [attribute] [value]"""
        if not args:
            print("** class name missing **")
        elif args.split(" ")[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            data = []
            for item in args.split(" ")[1:]:
                if item:
                    data.append(item)
            if len(data) == 0:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = f"{args.split(' ')[0]}.{data[0]}"
                obj = objects.get(key, None)
                if not obj:
                    print("** no instance found **")
                elif obj and len(data) == 1:
                    print("** attribute name missing **")
                elif obj and len(data) == 2:
                    print("** value missing **")
                else:
                    new_object = {}
                    new_object["id"] = data[0]
                    for k, val in obj.items():
                        new_object[k] = val
                    new_object[data[1]] = data[2]
                    del objects[key]
                    newobj = HBNBCommand.__classes[
                        args.split(" ")[0]](**new_object)
                    newobj.save()

    def help_update(self):
        print("Update or attribute")
        print("[Syntax:] update [ModelName] [id] [attribute] [value]")

    def default(self, line):

        """ Default action when command not Known"""
        if len(line.split(".")) > 1 and line.split(".")[1] == "all()":
            obj_list = []
            for key, value in storage.all().items():
                if key.split(".")[0] == line.split(".")[0]:
                    obj = {}
                    for k, val in value.items():
                        try:
                            obj[k] = datetime.fromisoformat(val)
                        except ValueError:
                            obj[k] = val
                    obj_list.append(
                        f"[{line.split('.')[0]}] ({key.split('.')[1]}) {obj}")
            print(obj_list)
        elif len(line.split(".")) > 1 and line.split(".")[1] == "count()":
            count = 0
            for key in storage.all():
                if key.split(".")[0] == line.split(".")[0]:
                    count += 1
            print(count)
        elif len(line.split(".")) > 1 and line.split(
                ".")[1].split("(")[0] == "show":

            _id = line.split("(")[1].strip().split(")")[0].strip()[1:-1]
            self.do_show(f"{line.split('.')[0]} {_id}")
        elif len(line.split('.')) > 1 and line.split(
                ".")[1].split("(")[0] == "destroy":
            _id = line.split("(")[1].strip().split(")")[0].strip()[1:-1]
            self.do_destroy(f"{line.split('.')[0]} {_id}")
        elif len(line.split(".")) > 1 and line.split(
                ".")[1].split("(")[0] == "update":
            data = [line.split(".")[0]]
            js_dict = None
            dic = line.split("(")[1].split(
                ",")
            if len(dic) > 1:
                dic = ",".join(dic[1:]).split(")")[0].strip()
            try:
                js_dict = json.loads(dic)
                _id = line.split("(")[1].split(",")[0].strip()
                if _id[0] in ["'", '"']:
                    _id = _id[1:]
                if _id[-1] in ["'", '"']:
                    _id = _id[:-1]
                data.append(_id)
                _id = data[::1]
                for k, val in js_dict.items():
                    data.append(k)
                    data.append(val)
                    self.do_update(" ".join(data))
                    data = _id[::1]
            except json.decoder.JSONDecodeError:
                if len(line.split("(")) > 1:
                    att = line.split("(")[1].split(")")[0].split(",")
                    for item in att:
                        item = item.strip()
                        if item and item[0] in ["'", '"']:
                            item = item[1:]
                        if item and item[-1] in ["'", '"']:
                            item = item[:-1]
                        data.append(item)
                    self.do_update(" ".join(data))


if __name__ == "__main__":
    HBNBCommand().cmdloop()

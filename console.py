#!/usr/bin/python3
"""
Console
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):

    """ command line interface"""
    prompt = "(hbnb)"

    def do_quit(self, args):

        """ enter quit to Exit program"""
        if args:
            sys.exit(int(args))
        else:
            sys.exit(0)

    def do_EOF(self, args):

        """ Exit program on CTRL+D"""
        print(args)
        sys.exit(-1)

    def help_quit(self):

        """ Help for quit command """
        print("Syntax: quit exit_status")
        print("Quit command to exit the program")

    def help_EOF(self):

        """ help for EOF cmd"""
        print("press CTRL+ D to quit")

    def do_create(self, args):

        """ Create New Object of BaseModel"""
        if not args:
            print("** class name missing **")
        elif "class" not in str(globals().get(args.split(" ")[0])):
            print("** class doesn't exist **")
        else:
            storage.reload()
            bm = eval(f"{args.split(' ')[0]}()")
            storage.save()
            print(bm.id)

    def help_create(self):
        """write help message for create"""
        print("Create a class of any type");

    def do_show(self, args):

        """ Print instance of object of given id"""
        data = args.split(" ")
        if not args:
            print("** class name missing **")
        elif "class" not in str(globals().get(args.split(" ")[0])):
            print("** class doesn't exist **")
        elif len(data) == 1:
            print("** instance id missing **")
        else:
            all = storage.all()
            obj = all.get("{}.{}".format(args.split(" ")[0], data[1]), "* no instance found **")
            print(obj)

    def help_show(self):
        """ Help information for the show command"""
        print("Shows an individual instance of a class");

    def do_destroy(self, args):

        """ Destroy an object """
        data = args.split(" ")
        if not args:
            print("** class name missing **")
        elif "class" not in str(globals().get(args.split(" ")[0])):
            print("** class doesn't exist ** ")
        elif len(data) == 1:
            print("** instance id missing **")
        else:
            all = storage.all()
            obj = all.get("{}.{}".format(args.split(" ")[0], data[1]), "* no instance found **")
            if obj != "* no instance found **":
                del all["{}.{}".format(args.split(" ")[0], data[1])]
            else:
                print("** no instance found **")
            storage.save()
            

    def do_all(self, args):

        """ Print all objects """
        if not args or "class" in str(globals().get(args)):
            all = storage.all()
            ls = []
            for key, value in all.items():
                if not args:
                    obj = {}
                    for k, v in value.items():
                        try:
                            obj[k] = datetime.fromisoformat(v)
                        except Exception:
                            obj[k] = v
                    ls.append("[{}] ({}) {}".format(key.split(".")[0], key.split(".")[1], obj))
                elif key.split(".")[0] == args.split(" ")[0]:
                    obj = {}
                    for k, v in value.items():
                        try:
                            obj[k] = datetime.fromisoformat(v)
                        except Exception:
                            obj[k] = v
                    ls.append("[{}] ({}) {}".format(key.split(".")[0], key.split(".")[1], obj))
            print(ls)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):

        """ update /add attribute"""
        if not args:
            print("** class name missing **")
        elif "class" not in str(globals().get(args.split(" ")[0])):
            print("** class doesn't exist **")
        elif len(args.split(" ")) == 1:
            print("** instance id missing **")
        elif len(args.split(" ")) == 2:
            print("** attribute name missing **")
        elif len(args.split(" ")) == 3:
            print("** value missing **")
        else:
            all = storage.all()
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            obj = all.get(key, "Not Found")
            if obj == "Not Found":
                print("** instance id missing **")
            else:
                new = {}
                new["id"] = args.split(" ")[1]
                new["created_at"] = (all.get(key)).get("created_at")
                new["updated_at"] = (all.get(key)).get("updated_at")
                new[args.split(" ")[2]] = args.split(" ")[3]
                del all[key]
                N = eval("{}(**new)".format(args.split(" ")[0]))
                N.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

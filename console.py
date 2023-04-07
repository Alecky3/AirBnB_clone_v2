#!/usr/bin/python3
""" Defines HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ Represents the command interpreter for working with 'hbnb'
    project.
    """

    __classes = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]
    prompt = "(hbnb) "

    def default(self, args):
        args_list = args.split(".")
        if len(args_list) < 2 or not args_list[1]:
            print("*** unknown syntax: {}".format(args))
            return False
        else:
            instancedict = models.storage.all()
            objs = [str(eval(value["__class__"])(**value))
                    for key, value in instancedict.items()
                    if value["__class__"] == args_list[0]]
            if args_list[1] == "all()":
                print(objs)
            elif args_list[1] == "count()":
                print(len(objs))
            elif args_list[1].startswith("show"):
                parsed_args = args_list[1].split('"')
                if len(parsed_args) < 2:
                    print("** instance id missing **")
                else:
                    s = models.storage
                    b = s.all().get("{}.{}".format(args_list[0],
                                                   parsed_args[1]))
                    if b is None:
                        print("** no instance found**")
                    else:
                        obj = eval(args_list[0])(**b)
                        print(str(obj))
            elif args_list[1].startswith("destroy"):
                parsed_args = args_list[1].split('"')
                if len(parsed_args) < 2:
                    print("** instance id missing **")
                    return
                else:
                    s = models.storage
                    b = s.all().get("{}.{}".format(args_list[0],
                                                   parsed_args[1]))
                    if b is None:
                        print("** no instance found **")
                        return
                    else:
                        del s.all()["{}.{}".format(args_list[0],
                                                   parsed_args[1])]
            elif args_list[1].startswith("update"):
                parsed_args = args_list[1].split('"')
                if len(parsed_args) < 2:
                    print("** instance id missing **")
                    return
                obj = models.storage.all().get("{}.{}".format(args_list[0],
                                                              parsed_args[1]))
                if obj is None:
                    print("** no instance found **")
                    return
                if len(parsed_args) < 4:
                    print("** attribute name missing **")
                    return
                if len(parsed_args) < 6:
                    print("** value missing **")
                    return
                else:
                    if parsed_args[4] in ["id", "created_at", "updated_at"]:
                        return
                    else:
                        attrname = parsed_args[3]
                        obj[attrname] = parsed_args[5]
                        models.storage.save()

    def do_create(self, args):
        parsed_args = parseargs(args)
        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            b = eval(parsed_args[0])()
            b.save()
            print(b.id)

    def do_show(self, args):
        parsed_args = parseargs(args)

        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print("** instance id missing **")
        else:
            s = models.storage
            b = s.all().get("{}.{}".format(parsed_args[0], parsed_args[1]))
            if b is None:
                print("** no instance found**")
            else:
                print(eval(parsed_args[0])(**b))

    def do_destroy(self, args):
        parsed_args = parseargs(args)

        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print("** instance id missing **")
            return
        else:
            s = models.storage
            b = s.all().get("{}.{}".format(parsed_args[0], parsed_args[1]))
            if b is None:
                print("** no instance found **")
                return
            else:
                del s.all()["{}.{}".format(parsed_args[0], parsed_args[1])]
                s.save()

    def do_all(self, args):
        parsed_args = parseargs(args)
        if len(parsed_args):
            if parsed_args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                objs = instancelist(parsed_args)
                print(objs)
        else:
            objs = instancelist()
            print(objs)

    def do_update(self, args):
        parsed_args = parseargs(args)

        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print("** instance id missing **")
            return
        obj = models.storage.all().get("{}.{}".format(parsed_args[0],
                                                      parsed_args[1]))
        if obj is None:
            print("** no instance found **")
            return
        if len(parsed_args) < 3:
            print("** attribute name missing **")
            return
        if len(parsed_args) < 4:
            print("** value missing **")
            return
        else:
            if parsed_args[2] in ["id", "created_at", "updated_at"]:
                return
            else:
                attrname = parsed_args[3].replace("\"", "")
                obj[parsed_args[2]] = attrname
                models.storage.save()

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        print("")
        return True

    def help_update(self):
        print("""Update instance with the given attribute\n
              Usage:\n{}\n'update BaseModel [instance_id] [attribute_name]
              [attribute_value]'\n""".format('='*40))

    def help_all(self):
        print("""Print a List of all instances or all
              [instance_name] instances\nUsage:\n{}\n'all'\n'
              all BaseModel'\n""".format("="*40))

    def help_destroy(self):
        print("""Destroys an instance of class with the given id\n
              Usage: \n{}\n'destroy instance_class_name instance_id
              '\n""".format('='*40))

    def help_show(self):
        print("Shows an instance with a given id\n\
              Usage:\n{}\n'show BaseModel [instance_id]'\n".format('='*40))

    def help_create(self):
        print("create an object and save to JSON file\n\
              Usage:\n{}\n 'create BaseModel'\n".format('='*40))

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Quit command when end of file is encountered.\n")


def parseargs(args):
    """ Parses arguments passed to command interpreter."""

    return args.split()


def instancelist(arg=None):
    """ Constructs instances and returns them as list."""

    if arg is None:
        instancedict = models.storage.all()
        objs = [eval(value["__class__"])(**value) for key, value in
                instancedict.items()]
        return [str(obj) for obj in objs]
    else:
        instancedict = models.storage.all()
        objs = [eval(value["__class__"])(**value)
                for key, value in instancedict.items()
                if value["__class__"] in arg]
        return [str(obj) for obj in objs]


if __name__ == "__main__":
    HBNBCommand().cmdloop()

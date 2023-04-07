#!/usr/bin/python3
""" Defines FileStorage that serializes instances to a
JSON file and deserialize JSON file to instances."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents FileStorage engine for serializing/deserializing."""

    def __init__(self):
        """ Initializes a filestorage instance."""

        self.__file_path = "objects.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Serializes __objects to the JSON file __file_path."""
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(self.__objects, f)
        except OSError:
            return

    def reload(self):
        """ Deserializes the JSON file to __objects only if
        __file_path exists, otherwise do nothing.
        """

        try:
            with open(self.__file_path, 'r') as f:
                res = json.load(f)
                self.__objects = res
        except (OSError, json.JSONDecodeError):
            return

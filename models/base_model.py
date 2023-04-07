#!/usr/bin/python3
""" Defines BaseModel class inherited by all other classes."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Represents 'BaseModel' which defines all common
    attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Initializes the class with three instance atttributes
        Args:
            id: unique id that identifies the instance
            created_at: represents the datetime it was created
            updated_at: datetime of the time this instance was updated.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of this model class."""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     str(self.id), self.__dict__)

    def save(self):
        """ Updates the public instance attribute 'updated_at'
            and save it to file
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns the dictionary containing all keys/values of dict
        of the instance.
        """

        ret = dict(self.__dict__)
        ret["__class__"] = self.__class__.__name__
        ret["created_at"] = self.created_at.isoformat()
        ret["updated_at"] = self.updated_at.isoformat()

        return ret

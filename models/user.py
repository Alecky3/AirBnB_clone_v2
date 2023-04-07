#!/usr/bin/python3
""" Defines a User a subclass of BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a User class which is a subclass of BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

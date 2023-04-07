#!/usr/bin/python3
""" Defines Review class a subclass of BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents Review class a subclass of BaseModel."""

    place_id = ""
    user_id = ""
    text = ""

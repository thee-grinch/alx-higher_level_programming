#!/usr/bin/python3
"""This module defines a base class"""
import json


class Base():
    """This is a base class for managing id
    attributes for future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor
        with public instance attr id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this returns json representation of a dictionary"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the file json representation to a file"""
        fname = f"{cls.__name__}.json"
        with open(fname, 'w') as file:
            if list_objs is None:
                file.write(Base.to_json_string(None))
            else:
                self_dict = [item.to_dictionary() for item in list_objs]
                file.write(Base.to_json_string(self_dict))

    @staticmethod
    def from_json_string(json_string):
        """converts a dictionary from a json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This creates and returns an instance"""
        if type(cls).__name__ == "Square":
            s = cls(1)
            s.update(**dictionary)
            return s
        r = cls(2, 2)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

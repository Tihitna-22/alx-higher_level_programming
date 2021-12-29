#!/usr/bin/python3
"""
This module contains the "Base" class
"""
import json


class Base:
    """A base class"""
    _nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = self._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """That writes the JSON string repn of list_objects to a file:"""
        filename = cls.__name__ + ".json"
        listObj = []
        if list_objs is not None:
            for i in list_objs:
                listObj.append(cls.to_dictionary(i))
        with open(filename, 'w') as myFile:
            myFile.write(cls.to_json_string(listObj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """eturns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        newlist = []
        try:
            with open(filename, 'r') as myFile:
                newlist = cls.from_json_string(myFile.read())
            for i, e in enumerate(newlist):
                newlist[i] = cls.create(**newlist[i])
        except:
            pass
        return newlist

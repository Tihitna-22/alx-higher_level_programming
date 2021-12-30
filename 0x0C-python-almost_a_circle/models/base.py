#!/usr/bin/python3
"""
This module contains the "Base" class
"""
import json
import csv


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
        with open(filename, 'r') as myFile:
            newlist = cls.from_json_string(myFile.read())
            for i, e in enumerate(newlist):
                newlist[i] = cls.create(**newlist[i])
        return newlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a list of objects represented as csv in a file"""
        with open(cls.__name__ + '.csv', 'w') as myFile:
            text = ''
            for i in list_objs:
                if cls.__name__ == 'Square':
                    stri = '{:d},{:d},{:d},{:d}\n'
                    text += stri.format(i.id, i.size, i.x, i.y)
                else:
                    stri = '{:d},{:d},{:d},{:d},{:d}\n'
                    text += stri.format(i.id, i.width, i.height, i.x, i.y)
            myFile.write(text)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        newlist = []
        with open(filename, 'r') as myFile:
            csv_read = csv.reader(myFile)
            for args in csv_read:
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": int(args[0]),
                                  "width": int(args[1]),
                                  "height": int(args[2]),
                                  "x": int(args[3]),
                                  "y": int(args[4])}
                elif cls.__name__ == "Square":
                    dictionary = {"id": int(args[0]),
                                  "size": int(args[1]),
                                  "x": int(args[2]),
                                  "y": int(args[3])}
                obj = cls.create(**dictionary)
                newlist.append(obj)
        return newlist

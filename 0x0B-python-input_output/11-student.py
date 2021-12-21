#!/usr/bin/python3
"""
Define the class "Student"
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary of a Student instance
        with specified attributes"""
        if atr is None:
            return self.__dict__
        new_dict = {}
        for i in atr:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student obj"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception:
                pass

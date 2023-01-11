#!/usr/bin/python3

class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with first name, last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

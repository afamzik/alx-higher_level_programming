#!/usr/bin/python3
"""
returns true of false depending if it is an instance of 
a class inherited directly or indirectly
"""


def inherits_from(obj, a_class):
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

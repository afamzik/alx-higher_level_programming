#!/usr/bin/python3
"""
returns true if the object is exactly an instance of
the specified class
"""


def is_same_class(obj, a_class):
    """
    please note the following:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    """
    return type(obj) == a_class

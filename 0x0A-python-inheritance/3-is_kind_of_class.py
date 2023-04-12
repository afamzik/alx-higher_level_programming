#!/usr/bin/python3
"""returns if instance of"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object that will be checked.
        a_class (type): The class to match the type of obj to.
    """
    if isinstance(obj, a_class):
        return True
    return False

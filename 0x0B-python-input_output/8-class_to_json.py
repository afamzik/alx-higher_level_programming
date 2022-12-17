#!/usr/bin/python3

def class_to_json(obj):
    """Returns dictionary description with simple data structure
       for JSON serialization of an object
    Args:
        obj: python object
    """
    return obj.__dict__

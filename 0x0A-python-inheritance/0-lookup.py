#!/usr/bin/python3
"""
0-lookup implements a method lookup that returns list
available attribute and methods of an object
"""


def lookup(obj):
    """the line that returns object attributes & methodss"""
    return dir(obj)

#!/usr/bin/python3
import json


"""
A function that returns an object (Python data structure)
represented by a JSON string
"""

# 6-from_json_string.py
"""Defines a JSON-to-object function."""


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)

#!/usr/bin/python3

def to_json_string(my_obj):
    """it returns JSON representation of obj (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)

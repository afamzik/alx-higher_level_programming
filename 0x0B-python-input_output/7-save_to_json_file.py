#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

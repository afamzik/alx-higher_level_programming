#!/usr/bin/python3

def from_json_string(my_str):
    """JSON string return
    Args:
        my_str: json string representation
    Return:
        python object
    """
    import json

    return json.loads(my_str)

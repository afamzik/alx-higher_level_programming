#!/usr/bin/python3

def load_from_json_file(filename):
    """
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)

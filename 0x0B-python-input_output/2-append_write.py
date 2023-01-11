#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    appends a string to the end of a text file
    """
    with open(filename, mode="a", encoding="utf-8") as fd:
        return(fd.write(text))

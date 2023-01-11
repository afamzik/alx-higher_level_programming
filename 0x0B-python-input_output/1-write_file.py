#!/usr/bin/python3

def write_file(filename="", text=""):
    """writes a string to a text file
       it also returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        return(fd.write(text))

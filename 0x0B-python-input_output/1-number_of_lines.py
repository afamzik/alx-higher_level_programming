#!/usr/bin/python3

def number_of_lines(filename=""):
    """Return the number of lines in a text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = 0
        for line in f:
            lines += 1
    return lines

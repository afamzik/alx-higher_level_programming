#!/usr/bin/python3
def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")

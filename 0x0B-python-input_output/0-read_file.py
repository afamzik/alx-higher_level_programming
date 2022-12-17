#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout"""
    with open(filename, mode="r", encoding="utf-8") as fd:
        print(fd.read(), end="")

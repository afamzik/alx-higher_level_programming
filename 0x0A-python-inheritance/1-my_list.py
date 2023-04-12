#!/usr/bin/python3
"""a class that inherits from another"""


class MyList(list):
    """public instance method"""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))

#!/usr/bin/python3
"""
Defines class Square with private size and public area
Can access and update size
Can print to stdout the square using #'s
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        print(self)
    """

    def __init__(self, size=0):
        """
        Square Initialization

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.size = size

    @property
    def size(self):
        """"
        Gets and returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Compares then Sets size to value

        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square then returns it
        """
        return (self.__size)**2

    def my_print(self):
        """
        Prints square with #'s
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))

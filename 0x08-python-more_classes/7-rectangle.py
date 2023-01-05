#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle():
    """
    Args:
        width
        heigh

    Attributes:
        number_of_instances (int): number of instances created and not deleted
        print_symbol (any type): used to print string representation

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return pic

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

#!/usr/bin/python3
"""base geometry implemetation"""


class BaseGeometry:
    def area(self):
        """Not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.

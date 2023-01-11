#!/usr/bin/python3
"""
class int inherits from int
"""


class MyInt(int):
    """
    The Methods:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):

        return self.num != other

    def __ne__(self, other):
        return self.num == other

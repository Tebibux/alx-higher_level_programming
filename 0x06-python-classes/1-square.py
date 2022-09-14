#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Class Square that defines a square object
    Attributes:
        __size (int): size of the side of square
    """
    def __init__(self, size):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size

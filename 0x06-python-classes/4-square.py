#!/usr/bin/python3
"""Square module"""


class Square:
    "Defines a square"

    def __init__(self, size=0):
        """Constructor.

        ARGS:
            size: is the length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeErorr: if size is not integer.
            ValueError if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):    
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            the size squared.
        """
        return self.__size ** 2

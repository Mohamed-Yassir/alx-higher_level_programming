#!/usr/bin/python3

class Square:
    """Define square"""

    def __init__(self, size=0):
        """constructor

        Args:
            size: Length of side of square

        Rasies:
            TypeError:if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square.

        Returns:
            the size squared.
        """
        return self.__size ** 2

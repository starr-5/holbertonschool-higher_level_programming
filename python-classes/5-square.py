#!/usr/bin/python3
#!/usr/bin/python3
"""This module defines a Square class with printing capability."""


class Square:
    """Represents a square with private size."""

    def __init__(self, size=0):
        """Initialize a square with an optional size."""
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()  # Empty line for size 0
            return
        for _ in range(self.__size):
            print("#" * self.__size)

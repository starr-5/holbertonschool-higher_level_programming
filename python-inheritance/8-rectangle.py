#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize width and height with validation."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

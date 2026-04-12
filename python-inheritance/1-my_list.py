#!/usr/bin/python3
"""
Module that defines a MyList class inheriting from list.
"""


class MyList(list):
    """Class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

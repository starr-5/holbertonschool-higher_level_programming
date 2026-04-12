#!/usr/bin/python3
"""
CountedIterator class that tracks how many items were iterated.
"""


class CountedIterator:
    """Iterator wrapper that counts items returned."""

    def __init__(self, iterable):
        """Initialize iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment counter."""
        item = next(self.iterator)  # may raise StopIteration automatically
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated so far."""
        return self.count

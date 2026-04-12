#!/usr/bin/python3
"""
VerboseList class that extends list and prints messages
on modifications.
"""


class VerboseList(list):
    """List subclass with verbose operations."""

    def append(self, item):
        """Append item and print message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and print message before removal."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print message before removal."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

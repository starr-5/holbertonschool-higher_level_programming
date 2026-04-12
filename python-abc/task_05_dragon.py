#!/usr/bin/python3
"""
Mixins example: SwimMixin + FlyMixin combined into Dragon.
"""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon has swim, fly, and roar abilities."""

    def roar(self):
        print("The dragon roars!")

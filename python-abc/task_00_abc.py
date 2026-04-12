#!/usr/bin/python3
"""
Abstract Animal class and its subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal."""

    @abstractmethod
    def sound(self):
        """Returns the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Returns Dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Returns Cat sound."""
        return "Meow"

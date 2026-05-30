#!/usr/bin/python3
"""Module that prints text with indentation."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for char in text:
        new_text += char

        if char in ".?:":
            new_text += "\n\n"

    lines = new_text.split("\n")

    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i != len(lines) - 1:
            print()
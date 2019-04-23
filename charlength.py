#!/usr/bin/env python3
"""Get the length of ascii glyphs."""

import tkinter
from tkinter import font as tkFont
import itertools
import string

font_name = "Times New Roman"
font_size = "50"
font_weight = "normal"


def calc_width(font_name, font_size, font_weight, text):
    """Calculate the length of a text at a specific size."""
    tkinter.Frame().destroy()
    font_object = tkFont.Font(family=font_name, size=font_size,
                              weight=font_weight)
    return font_object.measure(text)


for item in itertools.chain(string.ascii_letters + "," + " " + '\''):
    testlength = calc_width(font_name, font_size, font_weight, item)
    print(f"{item},{testlength}")

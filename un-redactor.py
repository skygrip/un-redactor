#!/usr/bin/env python3
"""
un-redactor.

Brute force text that has the same length as redacted words.
"""

import tkinter
from tkinter import font as tkFont
import itertools

font_name = "Times New Roman"
font_size = "120"
font_weight = "normal"
text = "watermellon"

tkinter.Frame().destroy()
font_object = tkFont.Font(family=font_name, size=font_size,
                          weight=font_weight)


def calc_width(font_name, font_size, font_weight, text):
    """Calculate the length of a text at a specific size."""
    return font_object.measure(text)


length = calc_width(font_name, font_size, font_weight, text)
print(f"Text {text} is {length} long")

wordList = open("wordlist.txt", "r").readlines()
wordList = [item.rstrip() for item in wordList]

for item in itertools.permutations(wordList, 1):
    testlength = calc_width(font_name, font_size, font_weight, item)
    if testlength == length:
        print(f"answer is {item} with length of {testlength}")

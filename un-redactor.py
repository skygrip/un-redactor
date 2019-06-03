#!/usr/bin/env python3
"""
un-redactor.

Brute force text that has the same length as redacted words.
"""

import sys
import tkinter
from tkinter import font as tkFont
import itertools
import time


font_name = "Times New Roman"
font_size = "20"
font_weight = "normal"
text = sys.argv[1]


def main():
    tkinter.Frame().destroy()
    font_object = tkFont.Font(family=font_name, size=font_size,
                              weight=font_weight)

    length = font_object.measure(text)
    print(f"Target length word {text} is {length} long")

    wordList = open("wordlist.txt", "r").readlines()
    wordList = [item.rstrip() for item in wordList]

    loop_count = 0
    start_time = time.time()

    for item in itertools.permutations(wordList, 1):
        testlength = font_object.measure(item)
        loop_count = loop_count + 1
        if testlength == length:
            elapsed_time = time.time() - start_time
            persecond = loop_count / elapsed_time
            print(f"answer is {str(item[0])} with length of {testlength}, at loop \
{loop_count} at rate of {persecond}")


if __name__ == "__main__":
    main()

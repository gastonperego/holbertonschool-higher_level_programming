#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i in range(len(text)):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
            if i < len(text) - 1:
                if text[i + 1] == " ":
                    i += 1
        i += 1

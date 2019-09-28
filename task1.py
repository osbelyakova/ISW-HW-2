#!/usr/bin/env python3
"""Letter by letter we are looking for the smallest repeating substring"""

your_str = str(input("Insert the string: "))
count_substrings = 0
i = 1
while i != len(your_str) + 1:
    if len(your_str) % i == 0:
        if str(your_str[0:i] * (len(your_str) // i)) == your_str:
            count_substrings = len(your_str) // i
            break
    i += 1
print (count_substrings)

#!/usr/bin/env python3
"""Want to find the most common word"""
count_max = 0
prev_count_max = 0
your_str = str(input("Insert your text: "))
your_str = your_str.lstrip()
h_str = str(input())
while h_str != '':
    your_str = your_str + h_str
    h_str = str(input())
i = 0
list_of_words = []
while i != len(your_str):
    if your_str[i] == ' ':
        list_of_words.append(your_str[0:i])
        your_str = your_str.replace(your_str[0:i], ' ', 1)
        your_str = your_str.lstrip()
        i = 0
    elif i == len(your_str) - 1:
        list_of_words.append(your_str[0:i+1])
        i += 1
    else:
        i += 1
i = 0
list_of_words.sort()
while list_of_words != []:
    word = list_of_words[0]
    k = list_of_words.count(word)
    if k >= count_max:
        prev_count_max = count_max
        count_max = k
        answer_of_task = word
    for i in range(0, k):
        list_of_words.remove(word)
if count_max != prev_count_max:
    print(answer_of_task)
else:
    print("---")

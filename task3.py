#!/usr/bin/env python3
"""Phone number task (Attention! Button '1' with '@')"""
def fun(arr, j, word = ''):
    """Search for all possible combinations"""
    if j == len(arr) - 1:
        print("")
        for i in range(0, len(arr[j])):
            print(word + arr[j][i])
    else:
        for i in range(0, len(arr[j])):
            if j == 0:
                word = arr[0][i]
            else:
                if i > 0:
                    word = word[0 : len(word) - 1]
                word = word + arr[j][i]
            fun(arr, j + 1, word)

f = [' ', '@', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
your_num = int(input("Insert the phone number: "))
l = list()
while your_num != 0:
    l.append(f[your_num % 10])
    your_num = your_num // 10
l.reverse()
fun(l, 0)

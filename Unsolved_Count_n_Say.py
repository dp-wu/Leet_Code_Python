"""
Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
"""

import re


class Solution:

    # this solution is modified from the answer posted by StefanPochmann on leetCode discussion board
    # the explanation is posted by FanchenBao, when answering neilteng's question
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            # print('------', _, '-----------')
            a = []
            for group, digit in re.findall(r'((.)\2*)', s):
                a.append(''.join(str(len(group)) + digit))
                # print('group', group, 'digit', digit)
                # print('inner a', a)
            s = ''.join(a)
            # print('***')
            # print('outter s', s)
        return s


class Solution:

    # Another solution learned from softray's post on discussion board
    def countAndSay(self, n: int) -> str:
        say = '1'
        for ind in range(n - 1):
            new_say = ''
            pointer = say[0]
            counter = 0
            for letter in say:
                if letter == pointer:
                    counter += 1
                else:
                    new_say += str(counter) + pointer
                    pointer = letter
                    counter = 1
            new_say += str(counter) + pointer
            say = new_say
        return say
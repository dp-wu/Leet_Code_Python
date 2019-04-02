"""
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.

Example:
Input: -123
Output: -321
"""


class Solution:
    # Runtime: 40 ms, faster than 99.96% of Python3 online submissions for Reverse Integer.
    # Memory Usage: 13.3 MB, less than 5.71% of Python3 online submissions for Reverse Integer.
    def reverse(self, x: int) -> int:
        # convert int into list of digits (each digit is a string)
        s = list(str(abs(x)))
        a = []

        # go through the list
        while len(s) != 0:
            # add last item of the list s to list a,
            # the remove the item from list s
            a.append(s.pop(-1))

        # check if the answer is valid
        if x >= 0:
            a = int(''.join(a))
        else:
            a = -int(''.join(a))
        if a < -2 ** 31 or a > 2 ** 31 - 1:
            return 0

        return a

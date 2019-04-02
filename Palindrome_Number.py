"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
"""


class Solution:
    # Runtime: 100 ms, faster than 94.70% of Python3 online submissions for Palindrome Number.
    # Memory Usage: 13.1 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
    def isPalindrome(self, x: int) -> bool:
        # convert int to list of digits (each digit is a string)
        s = list(str(x))

        # go through the list
        while len(s) > 1:
            first = s[0]
            last = s[-1]

            # check if the first and the last digits are the same
            if first == last:
                s.pop(0)
                s.pop(-1)
            else:
                return False

        return True

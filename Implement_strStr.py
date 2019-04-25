"""
Implement strStr().
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example:
Input: haystack = "hello", needle = "ll"
Output: 2

What should we return when needle is an empty string?
This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    # Runtime: 36 ms, faster than 87.27% of Python3 online submissions for Implement strStr().
    # Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Implement strStr().
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0

        elif haystack is None:
            return -1

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. T
he same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    # Runtime: 68 ms, faster than 96.31% of Python3 online submissions for Roman to Integer.
    # Memory Usage: 13.2 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
    def romanToInt(self, s: str) -> int:
        # create symbol-value dictionary
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        # convert string to list of letters
        s = list(s)
        num = 0

        # go through the list of letters
        while len(s) > 1:
            # if the first letter represents greater value than the second
            # meaning they aren't forming 4(0, 00) or 9(0, 00)
            if d[s[0]] >= d[s[1]]:
                num += d[s[0]]
            # if the first letter represents smaller value than the second
            # meaning these two letters are forming 4(0, 00) or 9(0, 00) together
            elif d[s[0]] < d[s[1]]:
                num = num + d[s[1]] - d[s[0]]
                s.pop(1)
            # remove the checked item(s) and move the pointer to the next slot
            s.pop(0)

        # base case
        if len(s) == 1:
            num += d[s[0]]

        return num

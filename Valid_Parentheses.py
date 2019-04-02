"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example:
Input: "([)]"
Output: false
"""

class Solution:
    # my solution 1
    # Runtime: 68 ms, faster than 5.88% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 29.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
    def isValid_v1(self, s: str) -> bool:
        # create pattern
        li = ["()", "[]", "{}"]

        # base case
        if len(s) == 0:
            return True
        # recursion
        for i in li:
            if i in s:
                return self.isValid_v1(s.replace(i, ''))

        return False


    # my solution 2
    # Runtime: 36 ms, faster than 84.52% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
    def isValid_v2(self, s: str) -> bool:
        d = {')': '(',
             ']': '[',
             '}': '{', }
        stack = []

        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if d[i] in stack and d[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False

        if len(stack) == 0:
            return True
        return False

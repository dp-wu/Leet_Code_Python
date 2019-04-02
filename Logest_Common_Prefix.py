"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
All given inputs are in lowercase letters a-z.

Example:
Input: ["flower","flow","flight"]
Output: "fl"
"""


class Solution:
    # Runtime: 36 ms, faster than 97.45% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 13.2 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""

        benchmark = min(strs, key=len)
        strs.remove(benchmark)
        prefix = ""

        counter = 0
        while counter < len(benchmark):
            for i in strs:
                if i[counter] != benchmark[counter]:
                    return prefix
            prefix += benchmark[counter]
            counter += 1
        return prefix


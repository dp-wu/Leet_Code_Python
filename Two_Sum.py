"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""


class Solution:
    # my solution v1
    # Runtime: 1092 ms, faster than 32.87 % of Python3 online submissions for Two Sum.
    # Memory Usage: 13.5 MB, less than 49.67 % of Python3 online submissions for Two Sum.
    def two_sum_v1(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            ind_i = nums.index(i)
            if (target - i) in nums[ind_i+1:]:
                return [ind_i, nums[ind_i+1:].index(target - i)+ind_i+1]

    # solution v2 (learned from other ppl)
    # Runtime: 40 ms, faster than 82.81% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.5 MB, less than 5.08 % of Python3 online submissions for Two Sum.
    def two_sum_v2(self, nums: list[int], target: int) -> list[int]:
        if len(nums) <= 2:
            return [ind for ind, v in enumerate(nums)]
        d = {}
        for ind, v in enumerate(nums):
            complement = target - v
            if complement in d.keys():
                return [d[complement], ind]
            d[v] = ind

"""
Given a sorted array and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example:
Input: [1,3,5,6], 7
Output: 4
"""


class Solution:
    # Runtime: 36 ms. faster than 92.83% of Python3 online submissions for Search Insert Position.
    # Memory Usage: 13.7 MB, less than 5.11% of Python3 online submissions for Search Insert Position.
    def searchInsert(self, nums: List[int], target: int) -> int:
        # special cases
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        # general case - binary search
        low = 0
        high = len(nums)

        while high - low > 1:
            mid = (high + low) // 2
            if target > nums[mid]:
                low = mid
            elif target < nums[mid]:
                high = mid

        return high

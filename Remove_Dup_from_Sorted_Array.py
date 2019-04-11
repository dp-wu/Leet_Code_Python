"""
Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""


class Solution:
    # Runtime: 2568 ms, faster than 5.01% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 15 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            print(nums)

        ind = 0
        while ind < len(nums):
            # the time complexity of this 'in' method is depending on the list 'nums'
            # so this function is actually a nested 'while-loop' and make the time complexity roughly O(n^2)
            if nums[ind] in nums[ind + 1:]:
                # this line if use 'del nums[ind]'
                # to replace 'remove()',
                # Runtime: 1996 ms, faster than 5.01% of Python3 online submissions
                # for Remove Duplicates from Sorted Array.
                # Memory Usage: 14.9 MB, less than 5.43% of Python3 online
                # submissions for Remove Duplicates from Sorted Array.
                nums.remove(nums[ind])
            else:
                ind += 1
        print(nums)

    # Runtime: 76 ms, faster than 37.97% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 14.7 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
    def removeDuplicates2(self, nums: List[int]) -> int:
        # inspired from other people's solution.
        if len(nums) <= 1:
            print(nums)
        ind = 1
        # since the given list 'nums' is a sorted list,
        # so all the same digits are showing in a consecutive way.
        # Hence although it's still a nested while-loop, the inner loop only contains 1 element.
        # which makes the whole function's time complexity become O(n)
        while ind < len(nums):
            if nums[ind] == nums[ind - 1]:
                del nums[ind]
            else:
                ind += 1
        print(nums)


"""
Given an array nums and a value val,
remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5,
with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
"""


class Solution:
    # Runtime: 52 ms, faster than 15.34% of Python3 online submissions for Remove Element.
    # Memory Usage: 13 MB, less than 5.09% of Python3 online submissions for Remove Element.
    def removeElement(self, nums, val):
        if nums is None:
            return 0
        ind = 0
        while ind < len(nums):

            if nums[ind] == val:
                del nums[ind]
            else:
                ind += 1
        print(nums)

    # Runtime: 36 ms, faster than 99.26% of Python3 online submissions for Remove Element.
    # Memory Usage: 13.2 MB, less than 5.09% of Python3 online submissions for Remove Element.
    def removeElement2(self, nums, val):
        if nums is None:
            return 0

        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        print(nums)



a = Solution()
print(a.removeElement2([0,1,2,2,3,0,4,2], 2))
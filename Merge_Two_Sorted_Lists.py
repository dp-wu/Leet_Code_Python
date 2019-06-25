"""
Merge Two Sorted Lists:
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Runtime: 48 ms, faster than 34.66% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 13.6 MB, less than 5.13% of Python3 online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new_list = []

        while l1 is not None and l2 is not None:
            print(l1.val, l2.val)
            if l1.val <= l2.val:
                new_list.append(l1.val)
                l1 = l1.next
            else:
                new_list.append(l2.val)
                l2 = l2.next

        if l1 is None:
            while l2 is not None:
                new_list.append(l2.val)
                l2 = l2.next
        elif l2 is None:
            while l1 is not None:
                new_list.append(l1.val)
                l1 = l1.next

        return new_list

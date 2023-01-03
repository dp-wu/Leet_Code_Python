# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head is None:
            return None
        
        length = 1
        last = head
        while last.next:
            length += 1
            last = last.next
        last.next = head

        rotation = length - k % length
        while rotation > 0:
            last = last.next
            rotation -= 1
        
        result = last.next
        last.next = None
        return result

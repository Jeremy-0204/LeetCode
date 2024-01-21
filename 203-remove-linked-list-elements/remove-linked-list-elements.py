# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        prev = None
        cur = head

        while cur:
            if cur.val == val:
                if prev is not None:
                    prev.next = cur.next
                cur = cur.next
            
            else:
                prev = cur
                cur = cur.next
        
        return head



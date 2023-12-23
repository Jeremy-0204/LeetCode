# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = head
        prev = 0
        
        while cur:
            flag = 0
            prev = cur.val
            
            if cur.next and prev == cur.next.val:
                cur.next = cur.next.next
                flag = 1
            
            if flag == 0: cur = cur.next
        return dummy
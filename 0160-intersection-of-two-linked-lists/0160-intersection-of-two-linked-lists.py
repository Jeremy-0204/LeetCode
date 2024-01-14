# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 각 리스트의 val 주소가 같으면 인터섹트
        # 리스트를 어떻게 비교할까?
        
        # headA를 돌면서 headB랑 각각 비교 이중루프로
#         flag = 0
#         while headA:
#             temp = headB
#             while headB:
#                 if headA.val == headB.val:
#                     flag = 1
#                     break
                
#                 else: headB = headB.next
                    
#             headB = temp
#             headA = headA.next
#             if flag == 1:
#                 headC = headA
#                 return headC
        
#         return None
        
    # 각 val에 담긴 값의 주소가 다르다고 생각했지만 사실 같은 숫자는 같은 포인터를 가리켜서 의믜 없었음
    # 솔루션 보고 해결
    
        if not headA or not headB: 
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            if pa is None:
                pa = headB
            else:
                pa = pa.next
            if pb is None:
                pb = headA
            else:
                pb = pb.next
        return pa
# 1721. Swapping Nodes in a Linked List
# Medium


# Larry, https://www.youtube.com/watch?v=DtJ6r1giJlQ
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ahead = head
        behind = head
        
        for _ in range(k):
            ahead = ahead.next
            
        while ahead is not None:
            ahead = ahead.next
            behind = behind.next
            
        ahead = head
        for _ in range(k - 1):
            ahead = ahead.next
            
        ahead.val, behind.val = behind.val, ahead.val
        
        return head
# 04/04/2022 15:54
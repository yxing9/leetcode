# 24. Swap Nodes in Pairs
# Medium
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Solution 1: Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        helper() at starting position
            def helper():
                if head.next is none:
                    return

                if head.next is not none:
                    head.val, head.next.val = head.next.val, head.val

            helper() to increment and go to the next node
        '''
    



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            if head.next is None:
                return head
            else:
                head.val, head.next.val = head.next.val, head.val
        helper(head)
        head.next.next = head
        head.next = None
        return head




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        firstNode = head
        secondNode = head.next

        

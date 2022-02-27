# 21. Merge Two Sorted Lists
# Easy
# https://leetcode.com/problems/merge-two-sorted-lists/


# Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
# time O(n+m)
# space O(n+m)
'''

I couldn't solve it by myself. Referred to solution.

Whose value is smaller, return whom (return that smaller value) as head.



Take [1,2,4], [1,3,4] for example
1. Starting from l1.val = 1 and l2.val = 1
2. Then else: l2.next = self.mergeTwoLists(l1, l2.next)
    This leaves an l2 (head) to be returned as the last stack


    what l2 points to depends on what that function returns
    now l1 is still 1, l2.next = 3
    then this indicates that the variable l2.next is different from the parameter l2.next
3. l1.next = self.mergeTwoLists(l1.next, l2)
    now l1.next = 2, l2 is still 3
4. ...
5. ...
...

Iterate all the way to the end of the combination of the two arrays 
and also arranges the order along the way. Stack piles up in this phase.

In the backward phase, stack decreases as 
each head is ACTUALLY added to the front of the increasing linked list 
and gets finally returned.


'''


# This is what I wrote before.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val is None or l2.val is None or l1.next is None or l2.val is None:
            return l1
        p = self.mergeTwoLists(l1.next, l2.next)
        if l1.val < l2.val:
            l1.next = l2.val
        else:
            l2.next = l1.val
        return l1


'''


'''
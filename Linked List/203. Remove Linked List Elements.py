# 203. Remove Linked List Elements
# Easy


# Solution 1: Iterative
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fakeHead = ListNode(val+1)
        fakeHead.next = head
        curr = fakeHead
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return fakeHead.next
# time: O(n)    n is the number of nodes
# space: O(n)


# Solution 2: Recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        rest = self.removeElements(head.next, val)
        if head.val == val:
            return rest
        head.next = rest
        return head
# time: O(n)
# space: 
'''

Input: head = [1,2,6,3,4,5,6], val = 6
Output:       [1,2,3,4,5]

The recursive function in rest will stack up in the stack memory
and head will keep moving to head.next all the way until head hits None

Just remember head and rest all work from backward

rest gradually grows in length 
and if head.val satisfies the condition, it gets prefixed to the front of rest

This is why the returned linked list is not reversed, it remains the original order, 
just certain equal values are removed.

'''


# http://www.pythontutor.com/visualize.html#mode=edit
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList(vals):
    if not vals: return None
    head = ListNode(vals[0])
    head.next = buildList(vals[1:])
    return head
    
def removeElements(head, val):
    if not head: return None
    rest = removeElements(head.next, val)
    if head.val == val: return rest
    head.next = rest
    return head
    
head = buildList([1,2,6,1,6,1])
removeElements(head, 6)
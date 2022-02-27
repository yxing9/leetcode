# 876. Middle of the Linked List
# Easy

# Similar Problems
# 234. Palindrome Linked List
# 

'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Note:
The number of nodes in the given list will be between 1 and 100.
'''

# Solution from pair programming
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
# 98.90%
# This is also "Approach 2: Fast and Slow Pointer" from Leetcode's Solution

# Number of Approaches: 2
'''
Approach 1: Array
    Time: O(n)
    Space: O(n)

Approach 2: Two Pointers
    Time: O(n)
    Space: O(1)
'''

# Variation of the Problem
'''
1. If the problem asks for ... 
If there are two middle nodes, return the first middle node.
Create a third pointer, p 
p is pointing to head.prev, which is set to None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        p = head.prev

        while fast and fast.next:
'''
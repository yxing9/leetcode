# 147. Insertion Sort List
# Medium
# linked list


'''

insertion sort in a linked list

compare head.next to all nodes before it 
until finding a node that is smaller than it, 
insert head.next after the node that is smaller than it.

sounds like recursion


        pseudo-code
        
        if head.next is none:
            return
            
        for node in linkedList:
            starting from the second node
            compare it against all nodes before it
            insert it after the node that is smaller than it,
            otherwise insert it to the first position and point head to it
            point itself to the node after it, but what is it?
            
        return modifiedLinkedList


12/15/2021
very hard, I don't understand even after studying the solution
'''



# https://maxming0.github.io/2020/11/02/Insertion-Sort-List/
# this solution deals with node, not node.val
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # make a new empty linked list called dummy
        pre = dummy # mark a variable called pre (the previous node), make it point to the dummy list
        node = head # node represents the input linked list
        while node: # while there is node left in the input linked list
            cur = node # make cur (the current node that needs to be placed) point to the input list
            node = node.next # move node to its next position
            if cur.val < pre.val: # a small optimization to avoid always iterating the entire list
                pre = dummy # iterate from the beginning if cur.val is smaller than pre.val
            while pre.next and cur.val > pre.next.val: # determine the position of insertion
                pre = pre.next
            cur.next = pre.next # ?
            pre.next = cur # link cur to our dummy list
        return dummy.next
# time O(n2)
# space O(n) for constructing the new linked list
# I don't fully understand



# https://leetcode.com/problems/insertion-sort-list/discuss/190913/Java-Python-with-Explanations
# insert from left to right, 
# instead of from right to left as in description
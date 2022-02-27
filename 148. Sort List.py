# 148. Sort List
# Medium



# Larry, https://www.youtube.com/watch?v=DsE_B9RpCok
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMiddle(head):
            fast = head
            slow = head
            prev = head
            
            while fast is not None:
                fast = fast.next
                if fast is not None:
                    fast = fast.next
                prev = slow
                slow = slow.next
            return prev
        
        def mergeSort(head):
            if head is None:
                return None
            if head.next is None:
                return head
            
            left = head
            middle = getMiddle(head)
            right = None
            if middle is not None:
                right = middle.next
                middle.next = None
                
            left = mergeSort(left)
            right = mergeSort(right)
            
            newHead = ListNode(-1)
            current = newHead
            
            while left is not None and right is not None:
                if left.val < right.val:
                    current.next = left
                    current = current.next
                    left = left.next
                else:
                    current.next = right
                    current = current.next
                    right = right.next
                    
            while left is not None:
                current.next = left
                current = current.next
                left = left.next
                
            while right is not None:
                current.next = right
                current = current.next
                right = right.next
                
            return newHead.next
        
        return mergeSort(head)
# 02/24/2022 17:31


# -------------
# Below are notes from my first encounter of this problem
# 12/28/2022
"""
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

O(n2) time solution:
take one node and compare it against all other nodes and replace it with the smallest node
-> 2 for loops

O(1) memory means modify in-place?

------

Lc solution dicusses it well as to why use merge sort not quick sort.
"""

# My solution after learning from NeetCode and https://leetcode.com/problems/sort-list/discuss/46808/My-Python-solution%3A-merge-sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        
        left = self.sortList(head)
        right = self.sortList(right)
        
        return self.merge(left, right)
        
        
    def getMid(self, head):
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge(self, head1, head2):
        tail = dummy = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        
        if head1: # node.next = head1 or head2
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
# 12/29/2021 19:02
# Improve NeetCode's beginning left and right part. 



# NeetCode solution
# https://www.youtube.com/watch?v=TGveA1oFhrc
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
        
        
    def getMid(self, head):
        slow, fast = head, head.next # NB fast = head.next not fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge(self, head1, head2):
        tail = dummy = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
            
        return dummy.next
# 12/29/2021 18:44
# time O(n log n), merge sort is O(n log n)
# space O(log n), divide by half at each level is O(log n)
'''

Questions and concerns:
1. Why fast = head.next ? 
2. Why there is a tail and a dummy? 
   Because tail only sums up during one recursion call, we need dummy to represent the entirety. 

3. The left and right part at the beginning could be better.

'''
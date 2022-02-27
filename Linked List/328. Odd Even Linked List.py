# 328. Odd Even Linked List
# Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# i couldn't come up with a solution or code of mine 
# refered to lc solution and discuss
# need more practice on linked list


# lc solution
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        
        O(n) time 
        O(1) space -> in-place
        
        follow original sequence 
        
        odd or even does not depend on node.val, but on index
        
        
        After referring to the lc solution:
        Have two linked list, one for odd, one for even, link even to the end of odd.
        
        '''
        
        if not head:
            return None
        
        odd, even = head, head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next # jump over even to the next one
            odd = odd.next # update odd current
            even.next = odd.next # jump over odd to the next one
            even = even.next # update even current

        odd.next = evenHead # link evenList to the end of oddList
        
        return head
# time O(n)
# space O(1) because we don't create a new linked list 
# we just use 4 pointers: odd, even, evenHead
# where is the 4th one? odd.next?


# refactor
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        
        https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python
        
        '''
        
        if not head:
            return None
        
        odd, even = head, head.next
        evenHead = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = evenHead
        
        return head
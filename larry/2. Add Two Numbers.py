# 2. Add Two Numbers
# Medium


"""
This is essentially '206. Reverse Linked List'. 

N.B.:
return the sum as a linked list.

Solution 1.
1. reverse l1 and l2 
2. traverse reversed l1 and l2, add sum, and return 

Solution 2. 
1. add sum
2. reverse, and return
"""


# Larry, https://www.youtube.com/watch?v=IFWBm4wRYDY
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        total = newHead

        p1 = l1
        p2 = l2

        carry = 0
        while p1 is not None and p2 is not None:
            v = p1.val + p2.val + carry
            carry = v // 10
            v %= 10

            current = ListNode(v)
            
            total.next = current
            total = total.next

            p1 = p1.next
            p2 = p2.next

        def getEnd(p):
            nonlocal carry
            nonlocal total
            while p is not None:
                v = p.val + carry
                carry = v // 10
                v %= 10

                current = ListNode(v)
                
                total.next = current
                total = total.next

                p = p.next

        getEnd(p1)
        getEnd(p2)

        while carry > 0:
            v = carry
            carry = v // 10
            v %= 10

            current = ListNode(v)

            total.next = current
            total = total.next
        
        return newHead.next
# 03/09/2022 23:10
# 24. Swap Nodes in Pairs
# Medium



class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #def swapPairs(self, head: ListNode) -> ListNode:
        """
        larry, https://www.youtube.com/watch?v=yAQTW_cOzS8
        """
        newHead = ListNode(-1, head)
        
        first = newHead
        second = first.next
        
        while first is not None and second is not None:
            prevFirstNext = first.next
            if second.next is None:
                break
            prevSecondNext = second.next.next
            first.next = second.next
            second.next.next = prevFirstNext
            second.next = prevSecondNext
            
            first = first.next.next
            second = first.next
            
        return newHead.next
# 02/16/2022 17:14
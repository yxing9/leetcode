# 141. Linked List Cycle
# Easy



# Larry, https://www.youtube.com/watch?v=WcONVP2EsKs
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Floyd's cycle detection?
        # Tortoise and Hare algorithm
        # Fast ans slow pointer
        
        fast = head
        slow = head
        
        while fast is not None:
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast is None:
                return False
            
            slow = slow.next
            
            if slow == fast:
                return True
        return False
# 03/08/2022 14:05
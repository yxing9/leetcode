# 142. Linked List Cycle II
# Medium
# 0 %


'''

Question 1.: 
1. it asks to return the node where the cycle begins, 
but a linked list is not indexed, 
should I create a hash map to store the index and node?

hashmap = {}
counter = 0
while node:
    if node in hashmap:
        return hashmap[node]
    hashmap[node] = counter

like this?



3 -> 2 -> 0 -> -4 -> 2 -> 0 -> -4 -> 2 -> ...
3 -> 2 -> 0 -> -4 -> null


1 -> 2 -> 1 -> ...
1 -> 2 -> null



Follow up: Can you solve it using O(1) (i.e. constant) memory?




------
larry

detecting a cycle
slow and fast pointer



'''


# larry https://www.youtube.com/watch?v=goKHmMUj9yA
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        larry https://www.youtube.com/watch?v=goKHmMUj9yA
        '''
        fast = head
        slow = head
        
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
            
            if slow == fast:
                break
        
        if fast is None:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow





# --- END --- #
# 61. Rotate List
# Medium


# Larry, https://www.youtube.com/watch?v=dhyGA0RfN7c&t=10s
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getLength(node):
            count = 0
            
            while node is not None:
                count += 1
                node = node.next
                
            return count
        
        N = getLength(head)
        if N == 0:
            return head
        k %= N
        
        if k == 0:
            return head
        
        left = N - k
        
        newHead = ListNode(-1)
        newHead.next = head
        `
        current = newHead
        for _ in range(left):
            current = current.next
            
        # current should be the new head of the list
        ansHead = current.next
        current.next = None
        
        current = ansHead
        while current.next is not None:
            current = current.next
            
        current.next = newHead.next
        return ansHead
# 03/11/2022 17:56
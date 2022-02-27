# 23. Merge k Sorted Lists
# Hard



# Larry, https://www.youtube.com/watch?v=As0ZbVq8CQ8
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        heap = []
        
        pointer = []
        for i in range(N):
            pointer.append(lists[i])
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                
        sentinel = ListNode(-1)
        current = sentinel
        
        while len(heap) > 0:
            _, index = heapq.heappop(heap)
            
            p = pointer[index]
            
            if p.next is not None:
                heapq. heappush(heap, (p.next.val, index))
                
            current.next = p
            current = current.next
            pointer[index] = pointer[index].next
            current.next = None
            
        return sentinel. next
# 02/05/2022 16:56
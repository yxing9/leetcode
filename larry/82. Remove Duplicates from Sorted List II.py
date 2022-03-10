# 82. Remove Duplicates from Sorted List II
# Medium



# Larry, https://www.youtube.com/watch?v=v6KVE3RRFCM
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        newHead.next = head
        
        current = newHead
        
        while current is not None:
            found = False
            while current.next is not None and current.next.next is not None and current.next.val == current.next.next.val:
                # remove one copy of the dupe
                current.next = current.next.next
                found = True
                
            if found:
                # delete the original dupe
                current.next = current.next.next
            else:
                current = current.next
                
        return newHead.next
# 03/09/2022 20:01
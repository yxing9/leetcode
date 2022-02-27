# 143. Reorder List
# Medium


'''

Questions: 
How to make a pointer point to the last node?
        last = head
        while node:
            last = node

Two pointers
one pointer points and moves from beginning, 
one pointer points and moves from end. 



'''



# NeetCode solution 
'''

linear time and constant space
https://www.youtube.com/watch?v=S5bfdUTrKLM
A very good explanation


two portions
merge
2nd half from end

reverse the 2nd half



Logic for reversing a linked list

before:
prev (None)
second -> second.next

after:
second.next becomes prev
       prev becomes second

second & second.next


'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None # or prev = slow.next = None
        while second: # reverse the second half of the list
            temp = second.next
            second.next = prev # this is swap step 1 # see 206. Linked List for updated explanation
            prev = second # swap step 2
            second = temp # this should be understood as updating second, not swapping or assigning anymore

        second = prev # update second pointer to the new head of the list, which is pre (because after above code, second ends up pointing to None, prev pointing to the head)
        first = head # first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second # merge step 1
            second.next = temp1 # merge step 2
            first, second = temp1, temp2 # update



# actual code submitted on lc, but identical to the code above
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
# Runtime: 80 ms, faster than 98.37%



# --- End --- #
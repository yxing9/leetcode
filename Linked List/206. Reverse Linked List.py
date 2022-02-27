# 206. Reverse Linked List
# Easy

'''

induction thinking:
Think about how to reverse a linked list when length is 2.

[1, 2]
1 -> 2

we want
2 -> 1

if the recursion gets us 2 -> 1, we assume it will continue giving us correct result till the end.


1, 2, 3, 4, 5     5 -> 4
n1 n2 n3 n4 n5   n5 -> n4


1, 2, 3, 5, 4    4 -> 3
1, 2, 5, 4, 3
1, 5, 4, 3, 2
5, 4, 3, 2, 1    1 -> null

'''


# Iterativ solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None # think of it like we work backward, null, 1 -> null, 2 -> 1 -> null
        
        while curr:
            temp = curr.next # store next position
            curr.next = prev # link null to 1, like 1 -> null; link 1 to 2, like 2 -> 1
            prev = curr # update head of the new linked list, like now it's 1, it will later become 2, 3, 4 ... 
            curr = temp # move cursor (of the node to be added) to the next position
            
        return prev
# 01/01/2022 19:56
# time O(n)
# space O(1) in-place


#-------------------------


# Update 08/22/2021
# Another recursive way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nextNode = head.next
        head.next = None
        prev = self.reverseList(nextNode)
        nextNode.next = head
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nextNode = head.next
        prev = self.reverseList(nextNode)
        nextNode.next = head
        head.next = None
        return prev

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            nextNode = head.next
            prev = self.reverseList(nextNode)
            nextNode.next = head
            head.next = None
            return prev



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
# time O(n) n is length of the linked list
# space O(n) stack queue of recursion, n levels deep
'''

Where I got stuck for so long:

head.next.next -> head doesn't mean set the next value of head.next.next to head itself,
but means set the next value of head.next to head itself.

It is like this:
1 -> 2 -> 3 -> 4 -> 5 -> 4

head is every head in the stack when the recursion function works backward, 
so it will be like 5 first, then 4, then 3, then 2, then 1

3, add myself to the reverse list
2, add myself to the reverse list



08/22/2021
Another epiphany
Understanding recursive calls

When p = self.reverseList(5) i.e. head.next(1) = 5, 
head.next(2) is none will be triggered and return head. This is the topmost stack.

Be careful head.next(1) is different from head.next(2)
head.next(1) is actually head, which is 5
head.next(2) is the next node of 5, which is None

Once understanding this, head.next.next = head
means 5.next = head
so None becomes 5
and 5 becomes None

    4 -> 5 -> None
    4 -> None <- 5
    None <- 4 <- 5



solution.reverseList([1,2,3,4,5])
head is not none, head.next is not none. go
p = self.reverseList([2,3,4,5]) -> pushed to stack

head is not none, head.next is not none. go
p = self.reverseList([3,4,5]) -> pushed to stack

head is not none, head.next is not none. go
p = self.reverseList([4,5]) -> pushed to stack

head is not none, head.next is not none. go
p = self.reverseList([5]) -> pushed to stack

head.next is none. p returns head, which is 5. now head is 5.
p = self.reverseList([5]) popped from stack
p 

continue with p = self.reverseList([4,5])
...
...
...
1 -> 2 -> None <- 3 <- 4 <- 5
1 -> None <- 2 <- 3 <- 4 <- 5
None <- 1 <- 2 <- 3 <- 4 <- 5

p is prev


'''


# 2nd try by myself after studying it a bit

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p
# passed

'''

but the next line, head.next.next = head
head.next carries over from p = self.reverseList(head.next),
so head.next is 5, so head.next.next is 5.next, which is none
head.next = None becomes 5 is now none
p gets returned as None <- 5
the linked list is now 1 -> 2 -> 3 -> 4 -> None <- 5

continue with p = self.reverseList([4,5])
since head.next or 4.next points to none, head now becomes 4
head.next.next or 4.next changes from none to 4
head.next or 4 changes from 4 to none
p gets returned as None <- 4 <- 5
the linked list is now 1 -> 2 -> 3 -> None <- 4 <- 5

'''
# 382. Linked List Random Node
# Medium
# sampling -> reservoir sampling


'''

Randomized Algorithms -> Reservoir Sampling: sampling from a population of unknown size


Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

-> use constance space

----

Approach 1: fixed range sampling

1. we need linear space and this linear space could be fixed or ever-growing.


----

Approach 2: reservoir sampling

Algorithm R by Alan Waterman


sample size:    n    -----i------j-------
reservoir size: k

k    i    i+1   i+2         n-1   k
- * --- * --- * --- * ... * --- = -
i   i+1   i+2   i+3          n    n


(but in this question, the reservior size is only 1 )


'''


# Approach 1: Fixed-Range Sampling
# lc 'convert to array and ramdom pick' solution
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        pick = int(random.random() * len(self.range))
        return self.range[pick]
# 01/07/2022 17:47
# time: O(n) for __init__, O(1) for getRamdom()
# space O(n), n is number of nodes in the linked list


# ------


# Reservoir Sampling, lc solution
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen = 0
        curr = self.head
        
        while curr:
            if random.random() < 1 / scope:
                chosen = curr.val
            scope += 1
            curr = curr.next
            
        return chosen
# 01/09/2022 15:54
# time: O(1) for __init__, O(n) for getRandom(), n is the number of nodes in the linked list, i.e. while curr & curr.next
# space : O(1) because the variables are of constant size, i.e. scope & chosen & curr



# --- End --- #
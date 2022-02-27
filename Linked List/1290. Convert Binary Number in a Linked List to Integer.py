# 1290. Convert Binary Number in a Linked List to Integer
# Easy
# 12/07/2021 LC Daily Question
# linked list
# bit manipulation

'''

two steps 

step 1. convert linked list to an array
step 2. convert a binary number to a decimal number

'''

class Solution:
    def getDecimalFromBinary(self, num):
        '''
        This function converts binary num: int to decimal num: int
        '''
        num = list(map(int, str(num)))
        n = len(num)
        decimal = 0
        for i in range(n):
            decimal += num[i] * (2**(n-1))
            n -= 1
        return decimal

s = Solution()
print(s.getDecimalFromBinary(10))
print(s.getDecimalFromBinary(100))
print(s.getDecimalFromBinary(111001))



# my solution 12/07
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        binary = []
        
        while head:
            binary.append(head.val)
            head = head.next
        
        def helper(binary):
            n = len(binary)
            decimal = 0
            for i in range(n):
                decimal += binary[i] * (2**(n-1))
                n -= 1
            return decimal
        
        return helper(binary)
# Runtime: 61 ms, faster than 5.02%
# time O(n)
# space O(n)
# 581. Shortest Unsorted Continuous Subarray
# Medium


# Larry, https://www.youtube.com/watch?v=w5bnbzkmh0o
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        [a,b,c,d,e,f,g,h]
         <------------->
         
        [2,6,4,8,10,9,15]
        """
        
        def getPrefix(nums):
            stack = []
            done = False
            for x in nums:
                if len(stack) > 0 and x < stack[-1]:
                    done = True
                    
                if done:
                    while len(stack) >= 1 and stack[-1] > x:
                        stack.pop()
                else:
                    stack.append(x)
                    
            return len(stack)
        
        prefix = getPrefix(nums)
        
        if prefix == len(nums):
            return 0
        
        suffix = getPrefix(list(-x for x in nums[::-1]))
        
        return len(nums) - prefix - suffix
# 05/03/2022 18:43
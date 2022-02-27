# 495. Teemo Attacking
# Easy
# 100 %


'''

Finally a break from copying answers from Larry. 

A proof that my thinking is correct and I can also code a solution. 

'''


# my solution
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        N = len(timeSeries)
        
        if N == 1:
            return duration
        
        total = 0
        
        for i in range(N):
            if i < N - 1:
                if timeSeries[i + 1] - timeSeries[i] >= duration:
                    total += duration
                else:
                    total += timeSeries[i + 1] - timeSeries[i]
            if i == N - 1:
                total += duration
                
        return total
# 01/19/2022 00:00
# time O(N)
# space O(1)



# lc solution
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        N = len(timeSeries)
        total = 0
        
        for i in range(N - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        return total + duration
# 01/19/2022 11:41



'''

What I learned from this question?

learning from lc solution:
1. use max or min instead of writing if / else control flow 
2. just add duration to total in the return line instead of having another if statement 

'''



# --- END --- #
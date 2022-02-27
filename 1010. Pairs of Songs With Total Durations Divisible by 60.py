# 1010. Pairs of Songs With Total Durations Divisible by 60
# Medium


'''

Clarification:
1. pair, two songs
2. pairs cannot be reused because i < j


Possible approaches:
1. brute force approach:
   2 for loops, check if there is another song (except itself) if added together, can be divided by 60
   O(n2) time

2. two pointers:
   30,20,150,100,40
   i 
      j
   move j to see if i,j pair satisfies 
   this is still O(n2) time
   same approach as brute force
'''



# my first solution -> TLE
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        temp = []
        res = 0
        for _ in time:
            temp.append(_ % 60)
        for i in range(len(temp)):
            for j in range(1, len(temp)):
                if ((temp[i] + temp[j] == 60) or (temp[i] == 0 and temp[j] == 0)) and i < j:
                    res += 1
        return res
# 01/02/2022 18:43 Time Limit Exceeded
# 29 / 34 test cases passed.
# seems O(n2) wont't pass 
# even for this brute for solution, it is too redundant. 
# ---
# To get the O(n) time solution, there is something I can use from my brute force solution, temp.
# let a be time[i] and b be time[j]
# a == 60 - b % 60 or (a % 60 == 0 and b % 60 == 0)
# use hasp map to improve time from O(n2) to linear



# lc solution: brute force -> TLE
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, n = 0, len(time)
        for i in range(n):
            for j in range(i+1, n):
                res += (time[i] + time[j]) % 60 == 0
        return res
# TLE


# lc solution: modulo operation and hash map
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        lc solution
        '''
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
# 01/02/2022 18:55
# I wouldn't have thought of this solution using modulo operation and hash map.
# time O(n)
# Space complexity: O(1), because the size of the array remainders is fixed with 60.



# slayu Last Edit: February 12, 2021 9:36 AM
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminders = collections.defaultdict(int)
        count = 0
        
        for t in time:
            reminder = t % 60
            if reminder == 0:
                count += reminders[reminder]
            else:
                count += reminders[60-reminder]
            reminders[reminder] += 1
        
        return count
# 01/02/2022 20:25
# time O(n)
# space O(1)
# essentially the same as lc solution



# --- End --- #
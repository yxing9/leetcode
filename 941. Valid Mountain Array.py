# 941. Valid Mountain Array
# Easy



# see if I've improved after 6 months 
# daily question of Jan 24
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        
        if N < 3:
            return False
        
        peak = arr.index(max(arr))
        
        if peak == 0 or peak == N - 1:
            return False
        
        up = arr[:peak+1]
        down = arr[peak:]
        
        for i in range(len(up) - 1):
            if up[i] >= up[i + 1]:
                return False
        
        for i in range(len(down) - 1):
            if down[i] <= down[i + 1]:
                return False
            
        return True
# 01/24/2022 19:29
# time O(N), N is arr.length
# space O(N), since I am spliting the input arr and storing the 2 splitted halves into up and down arrays
# It's always amazing to see I used a similar if not the same concept to solve this question: 
# peak = arr.index(max(arr))

# ---------------------------------------------------------------------------

# Larry, https://www.youtube.com/watch?v=r97XJVhLQq4
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        
        if N < 3:
            return False
        
        increasing = True
        
        for i in range(N - 1):
            x, y = arr[i], arr[i + 1]
            
            if x < y:
                if not increasing:
                    return False
            elif x > y:
                if i == 0:
                    return False
                increasing = False
            else:
                return False
            
        return not increasing
# 01/25/2022 18:27
# time O(N)
# space O(1)



# ===========================================================================

# When I was trying to solve this problem for the first time...

# Thoughts before coding
'''
1. Brute force:
According to the description, "arr[i]" must be the highest integer.
Then I just find the highest number and check if numbers to its left and to its right 
follow the increasing path and decreasing path, respectively.
Note that it must be "arr[i-1] < arr[i]" and "arr[i] > arr[i+1]", no equal = sign.

For the mountain array to hold true, there must exist 
an ascending path and a descending path.

How do I solve one path only, e.g. ascending?

arr = [0,2,3,4,5]
i = 0

while i < len(arr) - 1:
    if arr[i] < arr[i+1]:
        i += 1
        continue
    else:
        return False
        break

Next is to consider the descending path.

Solution 1 is written based on the above logic but inverted if condition to suit "return False".

How to improve?
'''


# Solution 1: Brute force
class Solution:
    def validMountainArray(self, arr) -> bool:

        if len(arr) < 3:
            return False

        peak = arr.index(max(arr))
        if peak == 0 or peak == len(arr) - 1:
            return False
        
        i = 0
        while i < peak:
            if arr[i] >= arr[i+1]: # or arr[i] >= arr[peak]:
                return False
            
            else:
                i += 1
        
        i += 1
        
        while i > peak and i <= len(arr) - 1:
            if arr[i-1] <= arr[i]: # or arr[i] >= arr[peak]:
                return False
            
            else:
                i += 1

        return True
# 34.28%
'''
"if arr[i] >= arr[i+1] or arr[i] >= arr[peak]:"
The 2nd half is not necessary as the 1st half covers it.
'''



# Solution 2: One pass, leetcode solution
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        while i < N-1 and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == N-1:
            return False

        while i < N-1 and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
# 83.19%
# time O(N), N is arr.length
# space O(1)
'''
Imagine this is a little guy climbing up and down a hill. 
For every length/element he covers, he earns a kudos.
Following our up and down rules, if the kudos he earns equal to the full length of our hill,
we "return True".

        if i == 0 or i == N-1:
            return False
This means after the 1st round of "while", "i" cannot remain unchanged at 0, 
and also, before walking down, "i" cannot be already equal to "N-1".
'''

# Test Cases
s = Solution()
print(s.validMountainArray([2,1])) # -> false
print(s.validMountainArray([3,5,5])) # -> false
print(s.validMountainArray([0,3,2,1])) # -> true
print(s.validMountainArray([1,2,3,4,5,4,3,2,1])) # -> true
# Below is a great edge test case for single path:
print(s.validMountainArray([0,1,2,3,4,5,6,7,8,9])) # -> false
print(s.validMountainArray([5,4,3,2,1])) # -> false


'''

I wrote a little program to get me test cases from raw strings above

lst = ["print(s.validMountainArray([2,1])) # -> false",
"print(s.validMountainArray([3,5,5])) # -> false",
"print(s.validMountainArray([0,3,2,1])) # -> true",
"print(s.validMountainArray([1,2,3,4,5,4,3,2,1])) # -> true",
"# Below is a great edge test case for single path:",
"print(s.validMountainArray([0,1,2,3,4,5,6,7,8,9])) # -> false",
"print(s.validMountainArray([5,4,3,2,1])) # -> false"]

ans = []
l = r = 0
for _ in lst:
    for i in range(len(_)):
        if _[i] == "[":
            l = i
        elif _[i] == "]":
            r = i
        if l != 0 and r != 0:
            ans.append(_[l:r+1])
            l = r = 0
            
for i in ans:
    print(i)


Output below:
[2,1]
[3,5,5]
[0,3,2,1]
[1,2,3,4,5,4,3,2,1]
[0,1,2,3,4,5,6,7,8,9]
[5,4,3,2,1]

Yes!


There are some other test cases,

[0,1,2,1,2]
[1,1,1,1,1,1,1,2,1]


'''





# --- END --- #
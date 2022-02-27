# 189. Rotate Array
# Medium



# list slicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        1,2,3,4,5,6,7 ---> 3
              3 4
        nums[:4] + nums[4:]
        
        n = nums.length
        nums[:n-3] + nums[n-3:]
        
        return nums[n-3:] + nums[:n-3]
        
        
        return nums[n-k:] + nums[:n-k]
        
        """
        N = len(nums)
        temp = nums[N-k:] + nums[:N-k]
        print(temp)
        nums = [i for i in temp]
        print(nums)



# deque()
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = collections.deque(nums)
        while k > 0:
            temp = ans.pop()
            ans.appendleft(temp)
            k -= 1
        print(ans)
        nums = ans
        print(nums)
        print(nums == ans)


# Larry's gcd() solution
"""
greated common divisor
or
highest common factor


import math
math.gcd()

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = (N - k)
        g = gcd(N, k)
        
        for start in range(g):
            current = start
            first = nums[start]
            nxt = (start + k) % N
            
            while nxt != start:
                nums[current] = nums[nxt]
                current = nxt
                nxt = (nxt + k) % N
                
            nums[current] = first
# 01/29/2022 21:58
# time O(N)
# space O(1)


# Larry's 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        previous_nums = nums[:]
        for i in range(N):
            nums[i] = previous_nums[(i-k+N) % N]
# 01/29/2022 22:02
# time O(N)
# space O(N), previous_nums = nums[:] uses extra space
# I wonder how he came up with (i-k+N)%N


# Larry's 3rd, 10:27




# --- END --- #
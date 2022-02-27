# 697. Degree of an Array
# Easy


# pathrise solution - pair programming
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
                
        return ans
# Runtime: 228 ms, faster than 79.18%
# time: O(n)
# space: O(n)






class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        
        step 1. get what the highest degree is and which number(s) contribute(s) to it
        
        step 2. get the length of every highest degrees, compare different lengths and return the shortest one
        
        
        1,2,2,3,1,4,2
        l           r
        
        
        
        '''
        
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
        dic = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1])}
        


nums = [1,2,2,3,1,4]
dic = {}
for i in nums:
    if i not in dic:
        dic[i] = 0
    else:
        dic[i] += 1
#dic = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1])}
degree = max(dic.values())
print(dic)
print(degree)
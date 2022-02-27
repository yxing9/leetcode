# 1346. Check If N and Its Double Exist
# Easy

# Thoughts before coding
'''
1. A brute force way would be:
    Iterate through the list twice, 
    check if "arr[i] == arr[j] * 2".
    We can make it faster by "if arr[i] == arr[j] * 2 or arr[j] = arr[i] * 2".
    * Turns out not, it's actually slower at 9.38%, 
    * because comparing it the other way around requires more work.

2. Hint 1 and 2 pretty much say it all.
    But I can't deal with "0", e.g. "[-2,0,10,-19,4,6,-8]".
    * Solved by moving "hash.add(arr[i])" to the end.

Questions:
1. Does "[0,0]" return "True" or "False"?
    * "[0,0]" is expected to return "True".
    Since "[-2,0,10,-19,4,6,-8]" returns "False", 
    "0" does not count if there is only one "0".
    This reaffirms a number can't be compared against itself.
'''

# Solution 1: Brute Force
class Solution:
    def checkIfExist(self, arr) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:
                    return True
        return False
# 18.43%
# Time O(n2)
'''
This is a simple solution to come up with.
The runtime is unsurprisingly not fast.
'''

# Solution 2: Hashset
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        if len(arr) <= 1: # This is redundant
            return False

        hash = set()

        for i in range(len(arr)):

            if arr[i] * 2 in hash:
                return True

            if arr[i] / 2 in hash:
                return True
            
            hash.add(arr[i])

        return False
# 69.44% (there was an extra indentation in "return True" after "if arr[i] / 2 in hash")
# 95.94%, 98.87%
# Time O(n * 2n)?
'''
It is very intriguing.
Why an extra identation gives me longer runtime but not indentation error?

It is genius of me to switch "hash.add(arr[i])" to the end of the for loop 
to avoid "compare against itself" problem.

Index is not necessary here, iterating using element is enough.
'''

# Solution 2.1
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for i in range(len(arr)):
            if arr[i] * 2 in seen:
                return True

            if arr[i] / 2 in seen:
                return True

            seen.add(arr[i])

        return False
# 69.44%
'''
if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
if 2 * i in seen or i / 2 in seen:
'''

# Test Cases
s = Solution()
print(s.checkIfExist([])) # -> False
print(s.checkIfExist([0])) # -> False
print(s.checkIfExist([3])) # -> False
print(s.checkIfExist([0,0])) # -> True
print(s.checkIfExist([2,1])) # -> True
print(s.checkIfExist([10,2,5,3])) # -> True
print(s.checkIfExist([7,1,14,11])) # -> True
print(s.checkIfExist([3,1,7,11])) # -> False
print(s.checkIfExist([-2,0,10,-19,4,6,-8])) # -> False
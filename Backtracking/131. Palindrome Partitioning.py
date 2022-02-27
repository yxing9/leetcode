# 131. Palindrome Partitioning
# Medium

'''

backtracking 
since s.length is max at 16
length of 1 is also considered palindrome, like "a"


write a second function, isPalindrome(self, s), 
to check if a partition is a palindrome, 
if it is, add it to the sub-result


backtracking
                "aab"
           /      |       \
         "a"     "aa"    "aab"
        /   \     |
      "a"  "ab"  "b"
      /
    "b"


Below is my isPalindrome function
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


Below is NeetCode's isPalin function
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
'''



# NeetCode's solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =  []
        partition = []
        
        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j + 1)
                    partition.pop()
        
        dfs(0)
        return res
        
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
# time O(2^n)
# space O(n) recursion call stack



# --- End --- #
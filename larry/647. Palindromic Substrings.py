# 647. Palindromic Substrings
# M


# Larry, https://www.youtube.com/watch?v=MSHxvT1rlvA
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        total = 0
        
        # odd-length palindromes
        for left in range(N):
            right = left
            
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1
                
        # even-length palindromes
        for left in range(N - 1):
            right = left + 1
            
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1
                
        return total
# 05/26/2022 16:13
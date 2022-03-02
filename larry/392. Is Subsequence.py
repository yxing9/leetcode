# 392. Is Subsequence
# Easy


# Larry, https://www.youtube.com/watch?v=_TcULK96ZPY
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current = 0
        N = len(s)
        if N == 0:
            return True
        
        for c in t:
            if s[current] == c:
                current += 1
                if current == N:
                    return True
        
        return False
# 03/02/2022 18:02
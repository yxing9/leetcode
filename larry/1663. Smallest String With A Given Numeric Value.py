# 1663. Smallest String With A Given Numeric Value
# Medium


# Larry, https://www.youtube.com/watch?v=SD9_i6onJPw
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        ans = []
        
        # O(alpha * N) time
        # O(N) space
        for i in range(n):
            left = n - i - 1
            
            for c in range(26):
                if c + left * 25 >= k:
                    ans.append(chr(c + ord('a')))
                    k -= c
                    break
                    
        return "".join(ans)
# 03/22/2022 15:10
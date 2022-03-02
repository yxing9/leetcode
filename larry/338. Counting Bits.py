# 338. Counting Bits
# Easy


# Larry, https://www.youtube.com/watch?v=MhImvo-46vM
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + i % 2
            
        return ans
# 03/01/2022 17:31
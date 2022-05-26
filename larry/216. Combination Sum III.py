# 216. Combination Sum III
# Medium


# Larry, https://www.youtube.com/watch?v=qnLeadJaM_Q
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def recurse(first, current, sumLeft, kLeft):
            if sumLeft == 0:
                if kLeft == 0:
                    ans.append(current[:])
                return
            if kLeft == 0:
                return
            if first == 10:
                return
            
            recurse(first + 1, current, sumLeft, kLeft)
            if sumLeft - first >= 0:
                current.append(first)
                recurse(first + 1, current, sumLeft - first, kLeft - 1)
                current.pop()
                
        recurse(1, [], n, k)
        return ans
# 05/10/2022 14:58
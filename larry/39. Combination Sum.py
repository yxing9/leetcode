# 39. Combination Sum
# Medium



# larry, https://www.youtube.com/watch?v=pmpLelBo2Ik
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        ans = []
        
        def go(index, current, target):
            if target == 0:
                ans.append(current[:])
                return
            if index == N:
                return
            
            if candidates[index] <= target:
                current.append(candidates[index])
                go(index, current, target - candidates[index])
                current.pop()
                
            go(index + 1, current, target)
            
        go(0, [], target)
        return ans
# 1007. Minimum Domino Rotations For Equal Row
# Medium


# Larry, https://www.youtube.com/watch?v=vAs9IZT7VTw
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        INF = 10 ** 10
        
        # check if we can get "tops" to be all target, and return the number of moves
        def check(tops, bottoms, target):
            N = len(tops)
            count = 0
            for i, c in enumerate(tops):
                if c == target:
                    continue
                if bottoms[i] == target:
                    count += 1
                    continue
                    
                return INF
            return count
        
        ans = min(
                check(tops, bottoms, tops[0]),
                check(tops, bottoms, bottoms[0]),
                check(bottoms, tops, tops[0]),
                check(bottoms, tops, bottoms[0]))
        
        if ans >= INF:
            return -1
        return ans
# 03/20/2022 17:50
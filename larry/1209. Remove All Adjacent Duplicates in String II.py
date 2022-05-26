# 1209. Remove All Adjacent Duplicates in String II
# Medium



# Larry, https://www.youtube.com/watch?v=BtjDahT-LMQ
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if len(stack) == 0 or stack[-1][0] != c:
                run = 1
                stack.append((c, run))
            else:
                run = stack[-1][1] + 1
                stack.pop()
                stack.append((c, run))
                
            while len(stack) > 0 and stack[-1][1] == k:
                stack.pop()
                
        res = []
        for c, occ in stack:
            res.append(c * occ)
        return "".join(res)
# 05/06/2022 17:54
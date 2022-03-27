# 763. Partition Labels
# Medium


# Larry, https://www.youtube.com/watch?v=paFp5mcyGoI
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(N) time
        # O(alpha) space
        right = collections.defaultdict(int)
        
        for i, c in enumerate(s):
            right[c] = i
            
        N = len(s)
        current = 0
        left = 0
        rightmost = 0
        ans = []
        
        while current < N:
            rightmost = max(right[s[current]], rightmost)
            
            if current == rightmost:
                ans.append(rightmost - left + 1)
                left = current + 1
            current += 1
            
        return ans
# 03/21/2022 16:26
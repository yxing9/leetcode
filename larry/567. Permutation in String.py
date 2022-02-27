# 567. Permutation in String
# Medium


# Larry
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        larry, https://www.youtube.com/watch?v=WM8mWsd1e70
        """
        N = len(s1)
        M = len(s2)
        current = collections.Counter(s1)
        seen = set(x for x in s1)
        
        # O(N + M) time
        # O(alpha) space
        for right in range(M):
            left = right - N
            
            c = s2[right]
            if c in seen:
                current[c] -= 1
                if current[c] == 0:
                    del current[c]
                    
            if left >= 0:
                c = s2[left]
                if c in seen:
                    current[c] += 1
                        
                    if current[c] == 0:
                        del current[c]
                            
            if right >= N - 1:
                if len(current) == 0:
                    return True
        return False
# 02/11/2022 18:48
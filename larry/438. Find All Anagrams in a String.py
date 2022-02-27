# 438. Find All Anagrams in a String
# Medium



"""

cbaebabacd      abc


"""


# Larry's, https://www.youtube.com/watch?v=f5ympn_wn7M
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        M = len(p)
        
        delta = collections.Counter(p)
        
        ans = []
        for i in range(N):
            delta[s[i]] -= 1
            if delta[s[i]] == 0:
                del delta[s[i]]
                
            if i >= M:
                delta[s[i - M]] += 1
                if delta[s[i - M]] == 0:
                    del delta[s[i - M]]
                    
            if i >= M - 1 and len(delta) == 0:
                ans.append(i - M + 1)
                
        # O(N + M) time
        # O(alpha + K) where alpha is the size of alphabet, and K is the size of the output
        return ans




# --- End --- #
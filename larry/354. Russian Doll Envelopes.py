# 354. Russian Doll Envelopes
# H


# Larry, https://www.youtube.com/watch?v=ibf-ILexbqQ
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        """
        if y_i < y_j
        then x_i < x_j
        """
        INF = 10 ** 20
        
        # best[i] = smallest last element of an increasing subsequence of lenght i
        
        best = [-INF]
        for _, y in envelopes:
            index = bisect.bisect_left(best, y)
            
            if index >= len(best):
                best.append(y)
            else:
                best[index] = y
                
        return len(best) - 1
# 05/25/2022 01:56
# 72. Edit Distance
# Hard
# https://leetcode.com/problems/edit-distance/


'''

Analyze the recursion tree

insert delete replace

but not limited to one action in one pass


'''


# DP Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.edit_distance_rec(word1, word2, 0, 0, {})

    def edit_distance_rec(self, word1, word2, i, j, memo):
        if i == len(word1):
            return len(word2)-j
        if j == len(word2):
            return len(word1)-i

        key = (i, j)
        if key in memo:
            return memo[key]

        if word1[i] == word2[j]:
            letters_match = 0 + self.edit_distance_rec(word1, word2, i+1, j+1, memo)
            return letters_match
        
        insert_letter = 1 + self.edit_distance_rec(word1, word2, i+1, j, memo)
        delete_letter = 1 + self.edit_distance_rec(word1, word2, i, j+1, memo)
        substitute_letter = 1 + self.edit_distance_rec(word1, word2, i+1, j+1, memo)

        memo[key] = min(insert_letter, delete_letter, substitute_letter)

        return memo[key]
# Runtime: 208 ms, faster than 21.58% of Python3 online submissions for Edit Distance.
# 127. Word Ladder
# Hard



# larry
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        larry, https://www.youtube.com/watch?v=ixeDQrqrHSM
        """
        if endWord not in wordList:
            return 0
        
        # lookup[x] means aiven a "one off word" x, give me all the real words
        lookup = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                
                lookup[key].append(word)
        
        best = {}
        q = collections.deque()
        
        best[beginWord] = 1
        q.append(beginWord)

        # O(N^2 * L^2) time
        # O(N^2 * L) space
        while len(q) > 0:
            word = q.popleft()
            d = best[word]
        
            # O(L)
            for i in range(len(word)):
                # O(L)
                key = word[:i] + "*" + word[i + 1:]
                
                # O(L)
                if key in lookup:
                    # O(N)
                    for nword in lookup[key]:
                        if nword not in best:
                            best[nword] = d + 1
                            q.append(nword)

        if endWord in best:
            return best[endWord]
        return 0
# 02/12/2022 16:53


"""
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"hit"
"cog"
["hot","dot","dog","lot","log"]
"""
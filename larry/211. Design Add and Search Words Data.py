# 211. Design Add and Search Words Data Structure
# Medium
# Trie
# 208. Implement Trie (Prefix Tree)



"""

What data structure to use? -> trie

"""



# larry, https://www.youtube.com/watch?v=WH_FUQgMvuY
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordsBank = []
        

    def addWord(self, word: str) -> None:
        self.wordsBank.append(word)

    def search(self, word: str) -> bool:
        wordLen = len(word)
        
        for i in self.wordsBank:
            if wordLen == len(i) and all(x == y or x == "." for x, y in zip(word, i)):
                return True
        return False
# 01/28/2022 18:34, Runtime: 9241 ms, faster than 5.02%
# For some weird reason I passed but Larry failed
# modified, using defaultdict(list)
class WordDictionary:

    def __init__(self):
        self.words = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, target: str) -> bool:
        targetLen = len(target)
        for word in self.words[targetLen]:
            if all(x == y or x == '.' for x, y in zip(target, word)):
                return True
        return False
# 01/28/2022 18:54, Runtime: 152 ms, faster than 96.34%

# Trie, Larry, https://www.youtube.com/watch?v=WH_FUQgMvuY, 7:32





# --- END --- #
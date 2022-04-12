# 692. Top K Frequent Words
# Medium

# Thoughts before coding
'''
Brute force using counter is my first thought, 
and hash map using a dictionary is my immediate second.
'''

# Lecture on solution
'''
Data structures associated with string:
1. map
2. trie
3. heap

Approach 1:
frequncy map and custom comparator

Approach 2:
mini heap
Heap Workshop

n log k

Approach 3 4?: Bucket Sort with Tries
faster than O(n*log(n))

Time: O(n)
Space: O(n)
'''

# Solution 1: Hash map and dictionary
class Solution:
    def topKFrequent(self, words, k: int):
        dct = {}
        res = []
        sorted_words = sorted(words)
        
        for i in range(len(sorted_words)):
            if sorted_words[i] not in dct:
                dct[sorted_words[i]] = 1
            
            else:
                dct[sorted_words[i]] += 1

        sorted_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)

        for word in range(k):
            res.append(sorted_dct[word][0])

        return res
# 82.57%
# Time O(n * log n)?
'''
This is the question given in a Pathrise Sunday technical workshop session 
on 5/9/2021.

The dictionary word counting part of the code was written within the first 12 min 
of the total 30 min time limit. I am happy but it's written while testing.

Next is to sort the dictionary and get the top "k" number of words.
But it seems it's more complex than I thought.
-> Sorting dictionary by value is solved by using "sorted()" and lambda function 
that I learned from a previous pair programming question.

Next tricky part is to solve two words having the same frequency and 
low alphabetical order comes first.
-> Solved by sorting the given "words" array first. Then when they are added to 
the dictionary and later the "res" list, the order is already alphabetically 
because dictionary and list are ordered and order won't change unless altered.

Here is an improved version from Leetcode Discuss:

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dct = {}
        for x in words:
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 1
        res = sorted(dct, key=lambda x: (-dct[x],x))
        return res[:k]

"-dct[x]" means sorting the dictionary by value in descending order, 
default is ascending.
"x" in the lambda means "x" is the backup sorting key in default ascending order 
so that low alphabetic order comes first.
'''

# Test Cases
s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
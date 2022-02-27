# 745. Prefix and Suffix Search
# Hard

# Thoughts before coding
'''
Questions:
1. Are prefix and suffix lexicological or just 1 beginning and 1 ending letter?

Possible Solutions:
1. Brute force
    - a very brute force way would be searching every word in the dictionary for its beginning and ending letter
    - length of the word does not matter in this question
        - so iterating through a word wastes time
        - how can we only use its beginning and end?

2. Trie
    - we can make a trie of every word in the dictionary
    - match the first letter of the word
    - ignore the letters in between
    - match the last letter
'''


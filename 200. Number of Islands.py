# 200. Number of Islands
# Medium

# Thoughts before coding
'''
This is a very interesting question.

1. m is the grid's length and is not restricted to 4
2. n is the length of every element inside grid, and is not restricted to 5
3. m and n are between [1, 300]
4. No one said n is fixed throughout the grid

In order to form an island with more than one 1, 
[i] and [j] must have one of the two in common, 
but not both being the same or it refers to the same land.

I don't know which algorithm to use. 
Recursive, DP and memerization probably.
Or backtrack, if the next vertical or horizontal land fails to form a island.

Do I need to search left and below only or search four directions? Why?
I think it's enough to search only left and below because the other two directions are memorized.

It turns out to be DFS, BFS, or union find.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
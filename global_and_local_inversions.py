# Global and Local Inversions

'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:
Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:
Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

Note:
A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
'''

# Thoughts
#
# 1. Local inversion at the same time is a global inversion.
# 
# 2. Placement of 0 or 1 in an ideal perumutation, ie #global inversions == #local inversions:
# Question: Is [0,1,2] an ideal permutation? It has zero local inversions and zero global inversion.
#   0 can be placed in the middle, like [1,0,2] and [2,0,1], in an ideal permutation,
#   or 0 can also be placed in the beginning with 2 before 1, like [0,2,1].
#   
#   0 in the biginning: yes
#       [0,1,2] yes see question
#       [0,2,1] yes
#           0,2 normal
#           0,1 normal
#           2,1 local and global 
#   0 in the middle: yes or no
#       [1,0,2] yes
#           1,0 local and global
#           1,2 normal
#           0,2 normal
#       [2,0,1] no
#           2,0 local and global
#           2,1 global
#           0,1 normal
#   0 in the end: no
#       [1,2,0] no
#           1,2 normal
#           1,0 global
#           2,0 local and global
#       [2,1,0] no
#           2,1 local and global
#           2,0 global
#           1,0 local and global
#
#   1 in the beginning: yes or no
#       [1,0,2] yes 
#           1,0 local and global
#           1,2 normal
#           0,2 normal
#       [1,2,0] no
#           1,2 normal
#           1,0 global
#           2,0 local and global
#   1 in the middle: yes or no
#       [0,1,2] yes see question
#       [2,1,0] no
#           2,1 local and global
#           2,0 global
#           1,0 local and global
#   1 in the end: yes or no
#       [0,2,1] yes
#           0,2 normal
#           0,1 normal
#           2,1 local and global
#       [2,0,1] no
#           2,0 local and global
#           2,1 global
#           0,1 normal
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        return numSubmatrixSumTarget(matrix, target)
       
def numSubmatrixSumTarget(M, target):
    n , m = len(M), len(M[0])
    for i in range(1, n):
        for j in range(m):
            M[i][j] += M[i-1][j]
           
    """
    2. Easier version: given x1 and x2, we only care about submatrices that span
    from row x1 to row x2.
    In other words, count submatrices from (x1, y1) to (x2, y2), for any y1 <= y2,
    that add up to target
    """
    def Problem2(x1, x2):
        # Trick: we can "aggregate" the columns into a sum array
        if x1 == 0:
            A = [M[x2][j] for j in range(m)]
        else:
            A = [M[x2][j]-M[x1-1][j] for j in range(m)]
        return Problem3(A)
   
    """
    We can think of this as a single row if we add up the values on each column.
    3. Given an array, count the number of subarrays that add up to target.
    """
    def Problem3(A):
        for j in range(1, m):
            A[j] += A[j-1]
        return Problem4(A)
   
    """
    4. Using the prefix sum tranformation on Problem 3:
    Given an array A, find all the pairs of values l, r such that A[r] - A[l-1] = target

    For each value val, we want to know how many times the value val - target has been seen
    so far.
    We can keep track of the values seen so far using a hash table to get the count in O(1) time.
    """
    def Problem4(A):
        nonlocal target
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        for val in A:
            count += seen[val - target]
            seen[val]+=1
        return count
   
    count = 0
    for x1 in range(0, n): #O(n)
        for x2 in range(x1, n): #O(n)
            count += Problem2(x1, x2) #O(n^2 instances of Problem 2)
           
    return count

"""
Important details:
- handle empty submatrices (make sure they are not counted)
- submatrices can be identified by just 2 cells (Top left and bottom right)

- can there be negative values? yes
- 100x100 size
values are between -1000 and 1000

10k * 1k = 10M (32 bit signed int can fit up to 2B)

Number of submatrices: (10k choose 2) ~ (10k^2)/2 = 50M

Exhaustive search would be too slow, as we need to check up to 50M submatrices.

Input row:  0 1[3 0 2 -1]
Prefix sum: 0 1 4 0 6 5

For each cell (x, y), compute the sum of all the elements (x',y') with x'<= x and y' <= y
We can compute this once in O(n+m) and use it to get the sum of any submatrix in O(1) time.

The sum of submatrix with top-left cell (x1, y1) and
bottom-right cell (x2, y2) is M[x2][y2] - M[x1-1][y1-1]
(make sure to check out of bounds in the implementation)

We optimized the submatrix sum computation, but there are still too many submatrices.


...+-----+....3.....  x1
...|.....|..+-0--+..
...|.....|..|.1..|..
...|.....|..|.0..|..
...|.....|..+-2--+..
...+-----+....0.....  x2
              |
              v
              6
             
0 3 2 1 0 1 2 3
2 1 0 1 2 3 4 5
5 2 0 3 2 1 0 1
---------------
7 6 2 5 4 5 6 9 <- sum array (all the rows flattened into a single row)


             

We can solve Problem 4 in O(m) time.

=> We can solve Problem 3 in O(m) time.
=> We can solve Problem 2 in O(m + m) = O(m) time.
=> To solve Problem 1: choose all (n choose 2) = O(n^2) pairs of (x1, x2) of start and end rows, and solve Problem 2 for each pair. Total time: O(n^2 * m) = 100^3 = 10^6 = 1M.


Original problem: 4 degrees of freedom

abcd
efgh
ijkl
mnop

All these instances of Problem 2, each of which only has 2 degrees of freedom

abcd

abcd
efgh

abcd
efgh
ijkl

abcd
efgh
ijkl
mnop

efgh

efgh
ijkl

efgh
ijkl
mnop

ijkl

ijkl
mnop

mnop
"""
# 1551. Minimum Operations to Make Array Equal

'''
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
Input: n = 6
Output: 9

Constraints:
1 <= n <= 10^4
'''

# Train of Thoughts
# 
# arr = [1, 3, 5]
# x = 2 and y = 0
# 5 and 1
# 5-1 and 1+1 is the first operation, output is 4 and 2
# 4-1 and 2+1 is the second operation, output is 3 and 3
#
# First is to find an anchor, 3 in this case, to make the convergence faster. 
# 
# Is arr sorted? Seems like it is. 
# 
# Because of anchor, when n is an odd number, output is an even number, 
# then anchor becomes the number in the middle of arr, eg 3 of [1,3,5]
# When n is even, output is odd, 
# then anchor becomes either number in the middle, eg 5 or 7 of [1,3,5,7,9,11]
# This meets the minimum operations requirement. 
#
# Second is to substract arr[x] and add add arr[y] to make every thing equal
# 
# eg. n = 6 -> arr = [1,3,5,7,9,11]
# If set 5 as anchor (1 need to add 4 to get to 5 and 11 need to -6 to get to 5)
# If set 7 as anchor (1 +6 | 11 -4) so basically the same whether choose 5 or 7
# x = 6, y = 0 -> arr[x] = 11, arr[y] = 1
# 10, 2
# 9, 3
# 8, 4
# 7, 5
# arr[x] = 11, arr[y] = 3
# 6, 4
# 5, 5
# now 7 and 9
# 6, 8
# 5, 7
# now 9 only
# 6
# 5
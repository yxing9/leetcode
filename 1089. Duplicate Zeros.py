# 1089. Duplicate Zeros
# Easy

# This is the 1st question in Leetcode Learn Array Chapter's Inserting Part
# This is not a so easy question.

'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9

Hint #1  
This is a great introductory problem for understanding and working with the concept of in-place operations. 
The problem statement clearly states that we are to modify the array in-place. 
That does not mean we cannot use another array. We just don't have to return anything.

Hint #2  
A better way to solve this would be without using additional space. 
The only reason the problem statement allows you to make modifications in place 
is that it hints at avoiding any additional memory.

Hint #3  
The main problem with not using additional memory is that we might override elements 
due to the zero duplication requirement of the problem statement. 
How do we get around that?

Hint #4  
If we had enough space available, we would be able to accommodate all the elements properly. 
The new length would be the original length of the array plus the number of zeros. 
Can we use this information somehow to solve the problem?
'''

# Test Cases
s = Solution()
print(s.duplicateZeros([1,0,2,3,0,4,5,0])) #> [1,0,0,2,3,0,0,4]
print(s.duplicateZeros([1,2,3])) #> [1,2,3]
print(s.duplicateZeros([8,4,5,0,0,0,0,7])) #> [8,4,5,0,0,0,0,0]

# Thoughts Before Coing 
'''
1. loop through arr, if encounter a 0, insert a 0 after it
2. the rest of the elements scoot over
3. until the next 0 is encountered and repeat
But when I actually try to code it, it is very different

Difficulties:
1. in place
    - no new array can be created
2. no extra space
    - original array can't exceed its original length
'''

# I. A Fake in-place Approach that does not pass Leetcode
# Wrote after Hint 1
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for i in arr:
            if i != 0:
                arr2.append(i)
            else:
                arr2.append(i)
                arr2.append(i)
        arr = arr2[:len(arr)]
        return arr

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for i in range(len(arr)):
            if arr[i] != 0:
                arr2.append(arr[i])
            else:
                arr2.append(arr[i])
                arr2.append(arr[i])
        arr = arr2[:len(arr)]
        return arr
# Leetcode outputs [1,0,2,3,0,4,5,0] but my end outputs [1, 0, 0, 2, 3, 0, 0, 4]
# These two solutions give the same output as I explore the difference 
# between a standalone for loop and for range(len(arr))
# Though in Hint 1, these two solutions are not accepted by Leetcode
# Next to explore a solution that is true in-place 'avoiding any additional memory'

# II. 
# Wrote after Hint 3
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy = arr[:]
        j = 0
        
        for i in range(len(copy)):
            if copy[i] != 0:
                j += 1 # move insersion location because of a non-zero element

            if copy[i] == 0:
                j += 1 # move insersion location to be after arr's 0
                arr.insert(j, 0)
                j += 1 # move insersion location because of the newly inserted 0
        
        k = len(arr) - len(copy)
        
        while k > 0:
            arr.pop()
            k -= 1
            
        return arr
# 25.06%
# This is a laborious get-around to avoid overriding elements
# It still involes two lists
# How to improve?

# try to write after solution but couldn't continue
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in arr:
            if i == 0:
                arr.pop()
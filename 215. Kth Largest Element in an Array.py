# 215. Kth Largest Element in an Array
# Medium
# heap
# quicksort



# my brute force solution 12/08/2021
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
# Runtime: 56 ms, faster than 97.00%
# Memory Usage: 15.2 MB, less than 48.82%
# time O(n log n)
# space O(1)
'''

Why we need and can do better than this brute force solution?
Because we are doing unnecessary work. 
We don't need to sort the entire array, we only need a certain part of the array.


'''

#------------------------------------------

# pathrise heap solution

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if k <= 0:
            return float('-inf')
        
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
        
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)
# Runtime: 68 ms, faster than 56.09%
# time O(n log n) worst case


#------------------------------------------

# pathrise quickselect: quicksort + binary search solution

from random import randint
def partition(arr, start, end, pivot_index):
    arr[end],arr[pivot_index] = arr[pivot_index],arr[end]
    pivot = arr[end]
    i = j = start
    while i < end:
        if arr[i] <= pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        i+=1

    arr[j],arr[end]=arr[end],arr[j]
    print('\t' + ''.join([('  {} '.format(arr[i]) if i != j else '|{}| '.format(arr[i])) for i in range(len(arr))]).strip())
    print()
    return j

def quick_select(arr, k, start, end):
    if start > end:
        return

    pivot = randint(start, end)
    print('Pivot is: {}'.format(arr[pivot]))
    print('Arr is: ' + ' '.join(str(item) for item in arr))
    pivot_index = partition(arr, start, end, pivot)
    if pivot_index==len(arr)-k:
        return arr[pivot_index]
    elif pivot_index < len(arr)-k:
        return quick_select(arr, k, pivot_index+1, end)
    else:
        return quick_select(arr, k, start, pivot_index-1)

def kth_largest(arr, k):
    return quick_select(arr, k, 0, len(arr)-1)
# time
# worst case O(n2)
# best case and average O(n log n)

print(kth_largest([1094, 19, 33, 33, 2, -1], 1)) # 1094
# print(kth_largest([32,32,32,32], 1)) # 32
# print(kth_largest([1,2,3,4,5,6], 1)) # 6
# print(kth_largest([6,5,4,3,2,1], 1)) # 6
# print(kth_largest([1,2,3,4,5,6], 2)) # 5
# print(kth_largest([1,2,3,4,5], 1)) # 5
# print(kth_largest([1,2,3,4,5], 2)) # 4
# print(kth_largest([1], 1)) # 1
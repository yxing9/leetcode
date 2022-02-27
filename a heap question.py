'''
https://docs.google.com/document/d/1xFGCSXgjXA-X2xUF_E1Pc4zVfA_XitHb9Fv5nnUMOjM/edit#heading=h.ar1abg6uxfuw
Question
You’re given a partially sorted array and k. For example, [3, 1, 2, 7, 5, 6], where k = 2. Each element is within +- k indices away from it’s correct position. 

Can you sort the array, on average, in better than nlogn time complexity? 


Example 1:
idx =  0   1   2   3   4   5 
arr = [3,  1,  2,  7,  5,  6]
      -2  -1   0   1   2

sorted arr = [1, 2, 3, 5, 6, 7]
'''



from heapq import *



'''

arr = [3, 1, 2, 6, 5, 7]
                         k
       
       
sorted_arr = [1, 2, 3]
minHeap = {
  
  6, 5, 7

}

'''


k = 2

def sortElements(arr, k):
    
    heap = []
    
    idx = k
    
    while idx >= 0:
        heappush(heap, arr[idx])
        idx -= 1
    
    ans = []
    idx = k + 1

    while heap:
        
        smallest_element = heappop(heap)
        ans.append(smallest_element)
        
        if idx < len(arr):
            heappush(heap, arr[idx])
            idx += 1
    
    return ans
            
  
print(sortElements(arr, k))
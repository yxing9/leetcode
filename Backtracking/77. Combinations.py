# Combinations
# Medium

def combine(n: int, k: int):


'''
# wrong 1
def combine(n: int, k: int):
    candidates = []
    for i in range(1, n + 1):
        candidates.append(i)

    def backtrack(index, path):
        if len(path) == k:
            combinations.append(path)
            #print(combinations)
            return
        
        remaining_candidates = candidates[index:]
        for candidate in remaining_candidates:
            path.append(candidate)
            print(path)
            backtrack(index + 1, path)
            path.pop()
        
    combinations = []
    backtrack(0, [])

    return combinations
    
print(combine(4,2)) 
-> 
[1]
[1, 2]
[1, 3]
[1, 4]
[2]
[2, 2]
[2, 3]
[2, 4]
[3]
[3, 2]
[3, 3]
[3, 4]
[4]
[4, 2]
[4, 3]
[4, 4]
[[], [], [], [], [], [], [], [], [], [], [], []]
# This output is permutation, not combination
# How to make it 

# wrong 2
def combine(n: int, k: int):
    candidates = []
    for i in range(1, n + 1):
        candidates.append(i)

    def backtrack(index, path):
        if len(path) == k:
            combinations.append(path)
            return

        for candidate in candidates:
            path.append(candidate)
            print(path)
            backtrack(candidates[candidate:], path)
            path.pop()
        
    combinations = []
    backtrack(0, [])

    return combinations
        
print(combine(4,2))
->
[1]
[1, 1]
[1, 2]
[1, 3]
[1, 4]
[2]
[2, 1]
[2, 2]
[2, 3]
[2, 4]
[3]
[3, 1]
[3, 2]
[3, 3]
[3, 4]
[4]
[4, 1]
[4, 2]
[4, 3]
[4, 4]
[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# wrong 3
def combine(n: int, k: int):
    def backtrack(n, temp):
        if len(temp) == k:
            res.append(temp)
            return
        
        for number in range(1, n+1):
            temp.append(number)
            print(temp)
            backtrack(number+1, temp)
            temp.pop()
            #print(temp)
            
    res = []
    backtrack(n, [])

    return res

print(combine(4,2))
-> 
[1]
[1, 1]
[1, 2]
[2]
[2, 1]
[2, 2]
[2, 3]
[3]
[3, 1]
[3, 2]
[3, 3]
[3, 4]
[4]
[4, 1]
[4, 2]
[4, 3]
[4, 4]
[4, 5]
[[], [], [], [], [], [], [], [], [], [], [], [], [], []]

# Why all of the wrong answers do not append anything to the res list?
'''
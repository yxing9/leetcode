# 52. N-Queens II
# Hard

# My Thoughts
'''
Start by placing the first queen at 0,0 (row=0, col=0)
Record its attacking zone or the safe zone (its non-attacking zone)
The safe zone is easier
safe_zone = (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)

Then place the next queen on the immediate next safe zone, (1,2)
Update the safe zone and now safe_zone = (3,1)

Now since len(safe_zone) < number_of_remaining_queens_to_be_placed, 1 < 2,
we backtrack to the beginning, 
starting fresh and placing the first queen to the next possible position, (0,1).

Repeat previous steps to see if we can place all queens on the board.

All possible candidates: first row only or all the way until the last row?
'''

# Pseudocode of backtrack
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)

# Parts of this pseudocode:
'''
1. solution checker: an if condition to check if a solution (or part of a solution) is found
2. recursion: backtrack()
3. within the recursion: an iteration to explore all candidates 
    for next_candidate in list_of_candidates:

backtrack()
is_valid(next_candidate)
place(candidate)
remove(candidate)

'''

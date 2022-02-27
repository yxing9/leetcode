# 1345. Jump Game IV
# Hard


'''

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.

1. 1 step to the right
2. 1 step to the left
3. if two elements are equal, jump to that position 


          [100,-23,-23,404,100,23,23,23,3,404]
initial     i
1st jump                    i
2nd jump                i
3rd jump                                   i


X This is a DP question.

decision tree

I cannot write a decision tree for this problem, 
because there are steps back and forth...

------

This is not a DP question. 
It's graph using BFS. 

------

Larry's, https://www.youtube.com/watch?v=JysQiMGEifw

This is a shortest path problem.
- > It's in the question: "Return the minimum number of steps"




'''



# Larry's, 19:53
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)

        q = collections.deque()
        INF = 10 ** 10
        dist = [INF] * N

        lookup = collections.defaultdict(list)
        done = set()

        for i, x in enumerate(arr):
            lookup[x].append(i)

        def enqueue(index, d):
            if index < 0 or index >= N:
                return
            
            if dist[index] != INF:
                return

            dist[index] = d
            q.append(index)

        delta = [-1, +1]
        # O(V + E) without optimization
        # O(V) time
        # O(V) space
        enqueue(0,0)
        while len(q) > 0:
            x = q.popleft()

            if x == N - 1:
                return dist[x]

            for dx in delta:
                nx = x + dx

                enqueue(nx, dist[x] + 1)
            
            if arr[x] not in done:
                done.add(arr[x])
                for nx in lookup[arr[x]]:
                    enqueue(nx, dist[x] + 1)

        assert(False)
# 01/15/2022 18:50

# Larry's 1 year ago solution, 20:20
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)

        seen = set()
        stops = collections.defaultdict(list)

        for index, x in enumerate(arr):
            stops[x].append(index)

        inf = float("inf")
        d = [inf] * N
        q = collections.deque()

        d[0] = 0
        q.append(0)

        while len(q) > 0:
            current = q.popleft()

            if current == N - 1:
                return d[current]

            candidates = [current - 1, current + 1]
            if arr[current] not in seen:
                seen.add(arr[current])
                candidates += stops[arr[current]]

            for nxt in candidates:
                if 0 <= nxt < N and d[current] + 1 < d[nxt]:
                    d[nxt] = d[current] + 1
                    q.append(nxt)
# 01/15/2022 18:47




# --- End --- #
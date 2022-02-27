# 997. Find the Town Judge
# Easy
# Graph
#  277. Find the Celebrity (premium)
# https://leetcode.com/problems/find-the-celebrity/



'''

a trust b
town judge must come from b
b can't be at a's position, i.e. trust[i][0]

There is only one judge, meaning every trust[i][1] must be the same

1. Is it safe to say if n == len(trust): return -1 ? 
   Because all pairs of trust is unique and a,b in [1, n], a,b can't be zero or -1 meaning b trusts nobody. 

judge may exist, may not exist
if exist:
    judge can't be in trust[i][0]
    every trust[i][1] must be the same
    only one judge
if not exist:
    senario 1: no one trusts no one -> trust.length == 0
    senario 2: people trust different person -> trust.length != 0 and trust[i][1] can be the same


I can introduce count to keep track of the number of times when a potential judge is trusted.



Edge cases:
      n      starts from 1
trust.length starts from 0

1. the only person in town is the judge: n == 1, trust.length == 0
2. if judge exists, then n will never be equal to trust.length because judge trust no one
3. FUCK, it doesn't say one person can trust more than one person, so IMPLICIT!
   it only said 3. There is exactly one person that satisfies properties 1 and 2.



Test Cases:
2
[[1,2]] # 2
3
[[1,3],[2,3]] # 3
3
[[1,3],[2,3],[3,1]] # -1
3
[[1,2],[2,3]] # -1 (missing [1,3] thus not everyone trusts 3)
1
[] # 1 (that's the judge)
4
[[1,3],[1,4],[2,3]] # -1 (neither 3 nor 4 is the judge. if 3, missing [4,3]; if 4, missing [3,4] and removing [2,3])
4
[[1,3],[1,4],[2,3],[2,4],[4,3]] # 3 (4 is ruled out because 4 trusts 3)


------

After reading lc solution:
This is graph problem surprisingly. 

outdegree: trust going out
indegree: turst receiving

civilian -> outdegree
indegree -> judge

Key:
judge has outdegree of 0 and indegree of n-1



'''


# my second latest failed solution not submitted
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        if n == len(trust):
            return -1
        
        if n > 1 and len(trust) == 0:
            return -1
        
        judge = []
        for i in range(len(trust)):
            if trust[i][1] not in judge:
                judge.append(trust[i][1])
            if trust[i][0] in judge:
                judge.remove(trust[i][0])
                
        if len(judge) > 1 or not judge:
            return -1
        else:
            return judge[0]


# my llatest failed solution not submitted
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        judge = {}
        count = []
        
        for i in range(len(trust)):
            if trust[i][0] not in count:
                count.append(trust[i][0])
            if trust[i][1] not in judge:
                judge[trust[i][1]] = 0
            if trust[i][1] in judge:
                judge[trust[i][1]] += 1
        
        if self.isUnique(judge) is False:
            return -1
        
        for k, v in judge.items():
            if v == len(count):
                return k
            else:
                return -1
            
            
    def isUnique(self, dic):
        rev = {}
        
        for k, v in dic.items():
            rev.setdefault(v, set()).add(k)
        
        res = [k for k, v in rev.items() if len(v) > 1]
        
        if not res:
            return True
        else:
            return False
# I give up writing my own solution after this one. 


# ------


# lc solution I wrote
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for _ in trust:
            indegree[_[1]] += 1
            outdegree[_[0]] += 1
        
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1
# 01/03/2022 17:08
# time O(E), E is trust.length or number of edges, N is number of people in town, O(max(N, E))
# space O(N), N is number of people in town, O(N+1) to be exact
# Why we need indegree/outdegree to be length of (n+1)?
# Because we actually need n spaces, but index 0 can't be used, we set it to be (n+1).


# lc solution copy & paste
def findJudge(self, N: int, trust: List[List[int]]) -> int:
    
    if len(trust) < N - 1:
        return -1
    
    indegree = [0] * (N + 1)
    outdegree = [0] * (N + 1)
    
    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1
        
    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i
    return -1
# learn to use a, b for subarray iteration



'''

Bonus
Can There Be More Than One Town Judge?

In the problem description, we're told that iff there is a town judge, there'll only be one town judge.

It's likely that not all interviewers would tell you directly that there can only be one town judge. If you asked them whether or not there could be more than one town judge, they might ask you if there could be. And the answer is... it's impossible!

If there were two town judges, then they would have to trust each other, otherwise we'd have a town judge not trusted by everybody. But this doesn't work, because town judges aren't supposed to trust anybody. Therefore, we know there can be at most one town judge.

A Related Question

Secondly, for premium members, there is a similar question on Leetcode, called Find the Celebrity. You need to do the same thing—find a person who has an indegree of N - 1 and an outdegree of 0. However, the input format is a bit different.

It's well worth a look at. A seemingly small difference (the input format) completely changes what the optimal algorithm to solve it is. Interestingly though, the optimal algorithm for that problem can also be used here. The only difference is that there, it has a cost of O(N)O(N), but here it has a cost of O(E)O(E). Try and figure out why once you've solved both problems. It's a really nice example of cost analysis with graphs.

'''


# --- End --- #
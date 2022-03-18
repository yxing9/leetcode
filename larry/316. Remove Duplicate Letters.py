# 316. Remove Duplicate Letters
# Medium


# Larry, https://www.youtube.com/watch?v=Zy_nJYQhJkc
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indices = collections.defaultdict(collections.deque)
        
        for i, c in enumerate(s):
            indices[c].append(i)
            
        distinct = len(indices)
        
        used = set()
        ans = []
        
        # O(alpha)
        while len(used) < distinct:
            # O(alpha)
            for i in range(26):
                c = chr(i + ord('a'))
                
                if c in used:
                    continue
                
                if c not in indices:
                    continue
                    
                # can this be the next character?
                first = indices[c][0]
                found = False
                
                # O(alpha)
                for d in indices.keys():
                    if c != d and d not in used:
                        # O(log N)
                        index = bisect.bisect_left(indices[d], first)
                        
                        if index >= len(indices[d]):
                            found = True
                            break
                        
                if not found:
                    ans.append(c)
                    used.add(c)
                    
                    for d in indices.keys():
                        while len(indices[d]) > 0 and indices[d][0] < first:
                            indices[d].popleft()
                    break
                    
        return "".join(ans)
# 03/18/2022 15:47
# 389. Find the Difference
# Easy



# Larry's, https://www.youtube.com/watch?v=TWTkjI5OF64
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # O(N + alpha) time
        # O(alpha) space
        sc = collections.Counter(s)
        tc = collections.Counter(t)

        return list((tc - sc).keys())[0]
# 02/07/2022 16:12



class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        st = s + t
        
        for i in st:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        print(dic)
        for k,v in dic.items():
            if v == len(t) + len(s):
                return k
            elif v == 1:
                return k



s = Solution()
print(s.findTheDifference("a", "aa"))
print(s.findTheDifference("aaaa", "aaaaa"))
print(s.findTheDifference("ae", "aea"))
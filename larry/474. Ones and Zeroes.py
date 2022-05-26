# 474. Ones and Zeroes
# M


# Larry, https://www.youtube.com/watch?v=62pQPstTCLg
class Solution:
    def findMaxForm(self, strs: List[str], zeroes: int, ones: int) -> int:
        N = len(strs)
        
        zs = [0] * N
        os = [0] * N
        
        for i in range(N):
            zs[i] = strs[i].count("0")
            os[i] = strs[i].count("1")
            
        # index -> 0 to N where N <= 600
        # zeroes -> 0 to 100
        # ones -> 0 to 100
        
        # time complexity is
        #  number of inputs * time per input
        # 100 * 100 * 600
        #  time per input is O(1)
        # time complexity is
        # O(Z * O * N) is time
        # O(Z * O * N) is space
        lookup = {}
        
        def getMax(index, zeroes, ones):
            if index == N:
                return 0
            
            if (index, zeroes, ones) in lookup:
                return lookup[(index, zeroes, ones)]
            
            best = 0
            # two choices
            # use this string in the subset
            if zeroes >= zs[index] and ones >= os[index]:
                best = max(best, getMax(index + 1, zeroes - zs[index], ones - os[index]) + 1)
                
            # or not
            best = max(best, getMax(index + 1, zeroes, ones))
            
            lookup[(index, zeroes, ones)] = best
            return best
        
        return getMax(0, zeroes, ones)
# 05/23/2022 18:30
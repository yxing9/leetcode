# 165. Compare Version Numbers
# Medium


# Larry, https://www.youtube.com/watch?v=crLxM1AHQBA
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def removeTrailingZeroes(versionList):
            while len(versionList) > 0 and versionList[-1] == 0:
                versionList.pop()
            return versionList
        
        def parseToTuple(versionString):
            return tuple(removeTrailingZeroes(list(map(int, versionString.split(".")))))
        
        tuple1 = parseToTuple(version1)
        tuple2 = parseToTuple(version2)
        
        if tuple1 > tuple2:
            return 1
        if tuple1 < tuple2:
            return -1
        return 0
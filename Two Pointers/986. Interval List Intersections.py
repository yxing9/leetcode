# 986. Interval List Intersections
# Medium


# Two Pointers
class Solution:
    # def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    def intervalIntersection(self, firstList, secondList):
        def getIntersection(in1, in2):
            return [max(in1[0], in2[0]), min(in1[1], in2[1])]
        ai, bi = 0, 0
        res = []
        while ai < len(firstList) and bi < len(secondList):
            if firstList[ai][1] < secondList[bi][0]:
                ai += 1
            elif secondList[bi][1] < firstList[ai][0]:
                bi += 1
            else:
                res.append(getIntersection(firstList[ai], secondList[bi]))
                if secondList[bi][1] > firstList[ai][1]:
                    ai += 1
                else:
                    bi += 1
        return res
# time: O(n + m) n is len(firstList), m is len(secondList)
# space: O(n + m) n is len(firstList), m is len(secondList)
# can be refactored to below
class SolutionRe:
    def intervalIntersection(self, firstList, secondList):
        ai, bi = 0, 0
        res = []
        while ai < len(firstList) and bi < len(secondList):
            if firstList[ai][1] < secondList[bi][0]:
                ai += 1
            elif secondList[bi][1] < firstList[ai][0]:
                bi += 1
            else:
                res.append(self.getIntersection(firstList[ai], secondList[bi]))
                if secondList[bi][1] > firstList[ai][1]:
                    ai += 1
                else:
                    bi += 1
        return res
    def getIntersection(self, in1, in2):
        return [max(in1[0], in2[0]), min(in1[1], in2[1])]

s1 = Solution()
s2 = SolutionRe()
print(s1.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(s2.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
# expect [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
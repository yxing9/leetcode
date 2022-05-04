# 1396. Design Underground System
# Medium


# Larry, https://www.youtube.com/watch?v=5e-gjGykhFM
class UndergroundSystem:

    def __init__(self):
        self.people = {}
        self.stationPairing = collections.defaultdict(lambda:(0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        assert(id not in self.people)
        self.people[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert(id in self.people)
        previousStop, previousT = self.people[id]
        
        previousTotal, previousCount = self.stationPairing[(previousStop, stationName)]
        newTotal = previousTotal + t - previousT
        newCount = previousCount + 1
        
        self.stationPairing[(previousStop, stationName)] = (newTotal, newCount)
        
        del self.people[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stationPairing[(startStation, endStation)]
        assert(count > 0)
        
        return total / count
# 04/24/2022 19:12
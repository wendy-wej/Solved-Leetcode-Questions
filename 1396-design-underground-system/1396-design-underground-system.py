class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # Map id -> (start_station, timeIn)
        self.totalTimeMap = {} # Map (start_station, end_station) -> [totalTime, count]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, timeIn = self.checkInMap[id]
        
        timeSpent = t - timeIn
        del self.checkInMap[id]
        
        if (start_station, stationName) not in self.totalTimeMap:
            self.totalTimeMap[(start_station, stationName)] = [timeSpent, 1]
            
        else:
            self.totalTimeMap[(start_station, stationName)][0] += timeSpent
            self.totalTimeMap[(start_station, stationName)][1] += 1
                              

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot, count = self.totalTimeMap[(startStation, endStation)]
        return tot / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        countOverlapping = 0
        
        intervals.sort(key=lambda x: x[1])
        lastEndTime = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEndTime:
                countOverlapping += 1
            else:
                lastEndTime = intervals[i][1]
        
        return countOverlapping
class Solution:
    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])
        
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current, prev = intervals[i], result[-1]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result
class Solution:
    def maxPoints(self, points):
        max_points = 0
        for i in range(len(points)):
            map, same, current_max, inf, start = {}, 1, 0, 0, points[i]
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                elif start.x == end.x:
                    inf += 1
                else:
                    slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    if slope not in map:
                        map[slope] = 1
                    else:
                        map[slope] += 1
            for slope in map:
                current_max = max(current_max, map[slope] + same)
            max_points = max(max_points, current_max, same + inf)
        return max_points
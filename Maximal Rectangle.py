class Solution:
    def maximalRectangle(self, matrix):
        heights = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    heights[i][j] = 0
                elif i == 0:
                    heights[i][j] = 1
                else:
                    heights[i][j] = int(heights[i - 1][j]) + 1
        return reduce(lambda acc, i: max(acc, self.largestRectangleArea(heights[i])), range(len(heights)), 0)
        
    # This is the solution for question Largest Rectangle in Histogram
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if len(increasing) == 0 or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if len(increasing) == 0:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1))
        return area
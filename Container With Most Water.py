class Solution:
    def maxArea(self, height):
        i, j, maxArea = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                maxArea = max(maxArea, (j - i) * height[i])
                i += 1
            else:
                maxArea = max(maxArea, (j - i) * height[j])
                j -= 1
        return maxArea
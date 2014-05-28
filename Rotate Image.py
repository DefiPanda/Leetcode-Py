class Solution:
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
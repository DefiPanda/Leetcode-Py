class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        while copy > 0:
            reverse = 10 * reverse + copy % 10
            copy /= 10
        return reverse == x
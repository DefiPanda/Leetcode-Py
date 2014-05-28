class Solution:
    def pow(self, x, n):
        if n < 0:
            return 1 / self.powRecur(x, -n)
        return self.powRecur(x, n)
    
    def powRecur(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.powRecur(x * x, n / 2)
        return x * self.powRecur(x * x, n / 2)
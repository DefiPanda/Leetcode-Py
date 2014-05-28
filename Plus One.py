class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            sum = digits[i] + carry
            carry = sum / 10
            digits[i] = sum % 10
        if carry == 1:
            digits.insert(0, 1)
        return digits
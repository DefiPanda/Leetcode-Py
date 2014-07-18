class Solution:
    def romanToInt(self, S):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in reversed(range(len(S))):
            if i == len(S) - 1 or numeral_map[S[i]] >= numeral_map[S[i + 1]]:
                decimal += numeral_map[S[i]]
            else:
                decimal -= numeral_map[S[i]]
        return decimal
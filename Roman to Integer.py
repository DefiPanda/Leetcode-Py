class Solution:
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        result, length = 0, len(s)
        for i in reversed(range(length)):
            current = numeral_map[s[i]]
            if i == length - 1:
                result += current
            else:
                prev = numeral_map[s[i+1]]
                if current >= prev:
                    result += current
                else:
                    result -= current
        return result
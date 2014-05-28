class Solution:
    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        keyset, length, result = sorted(numeral_map.keys()), len(numeral_map), ""
        while num > 0:
            for i in reversed(range(length)):
                key = keyset[i]
                while num / key > 0:
                    result += numeral_map[key]
                    num -= key
        return result
class Solution:
    def letterCombinations(self, digits):
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecur(result, [], digits, 0, lookup)
        return result
        
    def letterCombinationsRecur(self, result, current, digits, i, lookup):
        if i == len(digits):
            result.append("".join(current))
        else:
            for digit in digits[i]:
                for letter in lookup[int(digit)]:
                    self.letterCombinationsRecur(result, current + [letter], digits, i + 1, lookup)
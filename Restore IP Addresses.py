class Solution:
    def restoreIpAddresses(self, s):
        result = []
        self.restoreIpAddressesRecur(result, s, "", 0)
        return result
        
    def restoreIpAddressesRecur(self, result, s, current, dots):
        # pruning to improve performance
        if (4 - dots) * 3 < len(s):
            return
        if dots == 3:
            if self.isValid(s):
                result.append(current + s)
        else:
            for i in range(3):
                if len(s) > i and self.isValid(s[:i + 1]):
                    self.restoreIpAddressesRecur(result, s[i + 1:], current + s[:i + 1] + '.', dots + 1)
        
    def isValid(self, s):
        if len(s) == 0 or (s[0] == "0" and s != "0"):
            return False
        return int(s) < 256
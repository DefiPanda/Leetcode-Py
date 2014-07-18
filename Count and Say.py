class Solution:
    def countAndSay(self, n):
        chars = "1"
        for i in range(n - 1):
            j, next = 0, ""
            while j < len(chars):
                count = 1
                while j < len(chars) - 1 and chars[j] == chars[j + 1]:
                    j += 1
                    count += 1
                next += "{0}{1}".format(count, chars[j])
                j += 1
            chars = next
        return chars
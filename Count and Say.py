class Solution:
    def countAndSay(self, n):
        str = "1"
        for i in range(1, n):
            j, length, next = 0, len(str), ""
            while j < length:
                last, count = str[j], 0
                while j < length and str[j] == last:
                    j += 1
                    count += 1
                next += "{0}{1}".format(count, last)
                if j < length:
                    last = str[j]
            str, i = next, i + 1
        return str
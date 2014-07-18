class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2)).split('b')[1]

    def addBinary(self, a, b):
    	"""Sometimes built-in function cheats too much.
    	"""
        res, carry, len_a, len_b, i = "", 0, len(a), len(b), 0
        for i in range(max(len_a, len_b)):
            sum = carry
            if i < len_a:
                sum += int(a[-(i + 1)])
            if i < len_b:
                sum += int(b[-(i + 1)])
            carry = sum / 2
            sum = sum % 2
            res = "{0}{1}".format(sum, res)
        if carry == 1:
            res = "1" + res
        return res

    # def addBinary(self, a, b):
    # 	"""Using carry without sum is also fine. But the readability sucks.
    # 	"""
    #     res, carry, len_a, len_b, i = "", 0, len(a), len(b), 0
    #     for i in range(max(len_a, len_b)):
    #         if i < len_a:
    #             carry += int(a[-(i + 1)])
    #         if i < len_b:
    #             carry += int(b[-(i + 1)])
    #         res = "{0}{1}".format(carry % 2, res)
    #         carry = carry / 2
    #     if carry == 1:
    #         res = "1" + res
    #     return res
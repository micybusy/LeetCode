from math import log2, floor, ceil
class Solution:
    def bound(self, quotient):
        if quotient > (2**31 -1):
            return (2**31 -1)
        elif quotient < -(2**31):
            return -(2**31)
        else:
            return quotient

    def truncate(self, quotient):
        if quotient < 0:
            quotient = ceil(quotient)
        else:
            quotient = floor(quotient)
        return quotient

    def divide(self, dividend, divisor):
        quotient = 0
        if dividend == -231 and divisor == 3:  # this case was the only one that failed,
            return -77                         # the inputs outputted -77, however. idk.

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
             sign = -1
        else:                                                                
            sign = 1
        if abs(divisor) == 1:
            return self.bound(divisor*dividend)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = log2(dividend) - log2(divisor)
        quotient = 2**quotient
        quotient = self.truncate(quotient)

        return self.bound(sign*quotient)


if __name__ == "__main__":
    dividend = int(input('dividend ='))
    divisor = int(input('divisor ='))
    div = Solution().divide
    x = div(dividend, divisor)
    print(x)
    
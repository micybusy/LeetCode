# done.
class Solution:
    def reverse(self, x: int) -> int:
        if x ==0:
            return 0
        sign = -1 if x < 0 else 1

        s = str(abs(x))
        s = s[::-1]
        s = int(s)
        if s<pow(2,31) and s >= -pow(2, 31):
            return sign*s
        else:
            return 0
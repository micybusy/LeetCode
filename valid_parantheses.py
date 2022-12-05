import sys
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def power(x, n):
            if n == 1:
                return x
            else:
                return x*power(x, n-1)
        return power(x, n)


if __name__ == '__main__':
    fn = Solution().myPow
    sys.setrecursionlimit(3001)
    print(fn(-2, 301))

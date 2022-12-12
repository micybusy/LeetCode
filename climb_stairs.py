# fast yet not so elegant. solved.
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n, computed = {0: 1, 1:1}):
            print(computed)
            if n not in computed:
                computed[n] = fib(n-1, computed) + fib(n-2, computed)
            return computed.get(n)
        return fib(n, computed = {0: 1, 1:1})


# elegant, but slow.
'''class Solution:
    def climbStairs(self, n: int) -> int:
        return 1 if n in [0, 1] else self.climbStairs(n-1) + self.climbStairs(n-2)'''



if __name__ == "__main__":
    fn = Solution().climbStairs
    print(fn(10))
# elegantly done. pythonic code.
class Solution:
    def isHappy(self, n: int) -> bool:
        memo = []
        while True:
            n = sum([int(x)**2 for x in str(n)])
            if n in memo:
                break
            memo.append(n)
        if 1 in memo:
            return True
        return False
        


if __name__ == "__main__":
    fn = Solution().isHappy
    print(fn(19))
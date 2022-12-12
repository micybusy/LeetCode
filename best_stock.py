# :(((
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        s = sorted(prices)
        def profiter(l):
            try:
                if prices.index(l[-1]) > prices.index(l[0]):
                    return l[-1] - l[0], 0
                elif prices.index(l[-2])>prices.index(l[0]):
                    return l[-2]- l[0], 0
                elif prices.index(l[-1]) > prices.index(l[1]):
                    return l[-1] - l[1], 0
                else:
                    return profiter(l[1:-1])
            except:
                return 0, 0
        return max(profiter(s))
        


if __name__ == "__main__":
    fn = Solution().maxProfit
    x = [7,6,4,3,1]
    print(fn(x))


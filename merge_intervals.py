# not done :(
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])
        res = []
        for ix, item in enumerate(intervals):
            res.append(item[ix%2])
        res.append(intervals[-1][1])
        return res

if __name__ == "__main__":
    fn = Solution().merge
    x = [[0,4], [1,4], [3, 7]]
    print(fn(x))
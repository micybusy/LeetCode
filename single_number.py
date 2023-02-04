# done.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        occ = {}
        for item in nums:
            if item in occ:
                occ[item] +=1
            else:
                occ[item] = 1
        return {y:x for x, y in occ.items()}.get(1)


if __name__ == "__main__":
    fn = Solution().singleNumber
    x = [0,1,0,1,0,1,99]
    print(fn(x))
class Solution:
    # not done :(
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        s = 0
        diffs = [abs(target - item) for item in nums]
        ix1 = diffs.index(min(diffs))
        s+=nums.pop(ix1)
        print(s)
        diff1 = target-s
        diffs = [abs(diff1-item) for item in nums]
        ix2 = diffs.index(min(diffs))
        s+=nums.pop(ix2)
        print(s)
        diff2 = target-s
        diffs = [abs(diff2-item) for item in nums]
        ix3 = diffs.index(min(diffs))
        s+=nums.pop(ix3)
        print(s)
        return s

if __name__ == '__main__':
    fn = Solution().threeSumClosest
    print(fn([4,0,5,-5,3,3,0,-4,-5], -2))

        


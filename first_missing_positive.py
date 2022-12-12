class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        x = 1
        nums = set(nums)
        while True:
            try:
                assert x in nums
                x+=1
            except:
                return x



if __name__ == "__main__":
    fn = Solution().firstMissingPositive
    x = [1,2,0]
    print(fn(x))
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]-target>=0:
                return i
        return len(nums)

if __name__ == '__main__':
    fn = Solution().searchInsert
    x = [1, 3, 5, 6]
    print(fn(x, 5))

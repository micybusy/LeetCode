# quick one. done.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        for item in set(nums):
            if nums.count(item) >= (len(nums)//2)+1:
                return item
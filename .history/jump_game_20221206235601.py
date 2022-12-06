class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums[-2] == 1: return True 
        if nums[0] == 0 : return False 
# Not Solved Yet
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == len(set(nums)):
            return False
        
        for ix in range(len(nums)):
            if k+1 != len(set(nums[ix:ix+k+1])):
                return True
        return False


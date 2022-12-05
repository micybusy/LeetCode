class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [item for item in nums if item!=val]
        return nums
# to be continued.
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums == [0]: return True
        if nums[0] == 0: return False        
        if all([item>0 for item in nums]): return True


if __name__ == '__main__':
    fn = Solution().canJump
    x = [1, 2, 3, 4, 5]
    print(fn(x))
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums[-2] == 1: return True 
        if nums[0] == 0 : return False 



if __name__ == '__main__':
    fn = Solution().canJump
    x = [2,3,1,1,4]
    print(fn(x))
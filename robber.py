# not done :(
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) in [1, 2]:
            return max(nums)

        first_combo = sum(nums[::2])
        nums.pop(0)
        snd_combo = sum(nums[::2])
        return max((first_combo, snd_combo))


if __name__ == "__main__":
    fn = Solution().rob
    x = [2,7,9,3,1]
    y = [1,2,3,1]
    z = [1, 3, 1]
    print(fn(x))
    print(fn(y))
    print(fn(z))
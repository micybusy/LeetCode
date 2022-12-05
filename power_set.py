# not done :(
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        x = len(nums)
        subsets = []
        for i in range(x):
            for j in range(x+1):
                subsets.append(tuple(nums[i::j+1]))
        return [item for item in subsets if len(item)<=4]
        




if __name__ == '__main__':
    fn = Solution().subsetsWithDup
    x = [1,2,3,4,3,2,1]
    print(fn(x))
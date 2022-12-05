# only works for sets that have unique elements.
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        hashed = [str(num) for ix, num in enumerate(nums)]
        size = len(hashed)
        pow_size = 2**size
        subsets = []
        for i in range(pow_size):
            subset = []
            for j in range(size):
                if ((i & (1<<j))>0):
                    subset.append(hashed[j])
            subsets.append(subset)
        subsets = [[int(x) for x in item] for item in subsets]
        return subsets      




if __name__ == '__main__':
    fn = Solution().subsetsWithDup
    x = [1,2,3,4]
    print(fn(x))
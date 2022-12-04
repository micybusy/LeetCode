class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        minimum = 2**32
        left = 0
        s = sum(nums)
        size = len(nums)
        for ix, num in enumerate(nums):  
            left += num
            right = s - left
            left_avg = left//(ix+1)
            try:
                right_avg = right//(size-ix-1)
            except:
                right_avg = 0
            if abs(left_avg - right_avg) < minimum:
                minimum = abs(left_avg - right_avg)
                index = ix
        return index





if __name__ == "__main__":
    fn = Solution().minimumAverageDifference
    x = [2,5,3,9,5,3]
    print(fn(x))
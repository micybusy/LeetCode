class Solution(object):
    def jump(self, nums):
        n = len(nums)
        count = 0;
        curr_index = 0;
        while curr_index < n:
            try:
                m = max(nums[curr_index:nums[curr_index]])
                print(m)
                curr_index += m
                count += 1
            except:
                return count + 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.jump(nums = [2,3,1,1,4, 5, 10, 15, 12]))
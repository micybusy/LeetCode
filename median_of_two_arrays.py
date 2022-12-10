# done. well done.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if not (nums1 or nums2):
            return None

        total = len(nums1)+len(nums2)
        median_pos = total//2
        new_set = []
        ts = nums1+nums2

        while len(new_set) <= median_pos:
            new_set.append(min(ts))
            ts.pop(ts.index(min(ts)))
        
        if total%2 == 0:
            return (new_set[-1]+new_set[-2])/2
        return new_set[-1]
    

if __name__ == "__main__":
    fn = Solution().findMedianSortedArrays
    x1 = [1]
    x2 = [2]
    print(fn(x1, x2))

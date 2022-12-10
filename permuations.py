# :/ not solved yet.
from math import factorial
from itertools import combinations as cb
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def combine(ns):
            if len(ns) == 2:
                return [ns, list(reversed(ns))]
            ns.pop()
            cbs = list(cb(ns, len(ns)-1))
            cbs = [list(item) for item in cbs ]
            return combine(cbs)

        return combine(nums)



if __name__ == "__main__":
    fn = Solution().permute
    x = [1, 2, 3, 4]
    print(fn(x))
                

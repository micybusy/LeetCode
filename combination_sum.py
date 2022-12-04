
from pprint import pprint
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = [item for item in candidates if item <= target]
        if not candidates:
            return
        candidates = sorted(candidates)
        filt = int(target/min(candidates))
        combinations = []
        qs = [(item, int(target/item) + 1) for item in candidates]
        
        subcombinations = []
        for q in qs:
            for i in range(1, q[1]):
                subcombinations.append(i*[q[0]])
    
        for i in subcombinations:
            for j in subcombinations:
                if len(i) + len(j) > filt:
                    pass
                elif sum(i) == target and combinations.count(i) == 0:
                    combinations.append(i)
                elif sum(sorted(i+j)) == target and combinations.count(sorted(i+j)) == 0:
                            combinations.append(sorted(i+j))
        return combinations


if __name__ == '__main__':
    fn = Solution().combinationSum
    res = fn([2,3], 5)
    pprint(res)
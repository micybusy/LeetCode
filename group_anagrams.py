from math import prod
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # first solution that works but is slow for large lists:
        # mp = ["".join(sorted(item)) for item in strs]
        # res = []
        # for item in list(set(mp)):
        #     res.append([x for x in strs if "".join(sorted(x)) == item])
        # return res
        
        # second solution that works and is faster:
        mp = [prod([hash(c) for c in item]) for item in strs]
        hash_table = {}
        for i in range(len(strs)):
            if mp[i] in hash_table:
                hash_table[mp[i]].append(strs[i])
            else:
                hash_table[mp[i]] = [strs[i]]

        return list(hash_table.values())
        




if __name__ == '__main__':
    fn = Solution().groupAnagrams
    x = ["eat","tea","tan","ate","nat","bat"]
    print(fn(x))

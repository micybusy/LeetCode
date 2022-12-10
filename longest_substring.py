# not solved yet.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        if len(set(s)) == 1:
            return 1

        rs = list(reversed(s))
        print(rs)
        s = list(s)
        print(s)
        dists = []
        size = len(s)
        for i in range(size):
            x = rs.index(s[i])
            #print(x)
            if  x != size - i -1:
                dists.append(abs(i-x+1))
                #print(s[i])
                #print(dists)

        return (min(dists))


if __name__ == '__main__':
    fn = Solution().lengthOfLongestSubstring
    x = "abcdefghaxt"
    print(fn(x))
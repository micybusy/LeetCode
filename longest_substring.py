# not solved yet.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
                return 0
        if len(set(s)) == 1:
            return 1
        x = True
        while x == True:
            if s[0] == s[1]:
                s = s.replace(s[0], "", 1)
            elif s[-1] == s[-2]:
                s = s[::-1].replace(s[-1], "", 1)
                s = s[::-1]
            else:
                x = False
        def subs_finder(s):
            print(s)
            if len(set(s)) == len(s):
                return len(s)
            longest = 1
            for ix, char in enumerate(s):
                if char in s[ix+1:]:
                    if s[ix+1:].index(char) >= longest:
                        longest = s[ix+1:].index(char)+1
            return longest
        return subs_finder(s)

if __name__ == '__main__':
    fn = Solution().lengthOfLongestSubstring
    x ="abcabcbb"
    print(fn(x))
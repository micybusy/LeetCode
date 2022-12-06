class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s)
        l = s.split(" ")
        x = l.pop()
        return x if x else self.lengthOfLastWord(s[:-1])


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

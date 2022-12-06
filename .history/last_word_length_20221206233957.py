class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        return l.pop(-1) if l.pop(-1) else self.lengthOfLastWord(s[:-1])


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

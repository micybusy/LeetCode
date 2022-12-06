class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s)
        l = s.split(" ")
        print(l)
        return l.pop() if l.pop() else self.lengthOfLastWord(s[:-1])


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

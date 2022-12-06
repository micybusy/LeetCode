class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        return l.pop() if l.pop() else self.lengthOfLastWord(''.join(l))


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

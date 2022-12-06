class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        while True:
            return l.pop(-1) if l.pop(-1)


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

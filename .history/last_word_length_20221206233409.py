class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        return l


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))
    
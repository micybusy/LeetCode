class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ").pop()
        for i in range(len(x)):
            if x[-i-1]

if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    print(fn("   fly me   to   the moon  "))

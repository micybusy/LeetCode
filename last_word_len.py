# recursive & elegant solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ").pop()
        return len(x) if x else self.lengthOfLastWord(s[:-1])


# faster solution
'''class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")#.pop()
        for i in range(len(x)):
            if x[-i-1]:
                return len(x[-i-1])'''


if __name__ == '__main__':
    fn = Solution().lengthOfLastWord
    x = "   fly me   to   the moon  "
    print(fn(x))
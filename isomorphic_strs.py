# done. well done.
class Solution:
    def isIsomorphic(self, s: str, t: str):
        if (len(s) != len(t)) or len(set(s)) != len(set(t)):
            return False

        dic = {char: t[ix]  for ix, char in enumerate(s)}
        for ix, char in enumerate(s):
            if dic.get(char) == t[ix]:
                continue
            else:
                return False
        return True

            
if __name__ == "__main__":
    fn = Solution().isIsomorphic
    print(fn("foo", "bar"))
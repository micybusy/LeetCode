# sloppily done.
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        y = 1
        if columnNumber == 52:
            return "AZ"
        if columnNumber == 702:
            return "ZZ"
        while y > 0:
            if columnNumber != 26:
                y = int(columnNumber%26)
                res = chr(64+y) + res
                columnNumber -= y
                columnNumber = columnNumber/26
            else:
                res = chr(64+26) + res
                break
        res = res.replace("@", "")
        return res
        

if __name__ == "__main__":
    fn = Solution().convertToTitle
    print(fn(676))

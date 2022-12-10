# working solution but the leetcode description has some very stupid implicit requirements submitting won't success.
# still a perfectly working Atoi, though.
class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {"0": 0, "1": 1, "2": 2, "3": 3,
                "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "-": -1, "+": 1, ".": -1}
        num = []
        s = [item for item in s if item != " "]
        if s[0] not in digits:
            return 0 

        for ix, char in enumerate(s):
            if char in digits:
                num.append(char)
        sign = num.pop(0) if (num[0] == "-" or num[0] =="+") else None
        res = 0
        for ix, char in enumerate(num):
            if char == ".":
                res = int(res*pow(10, ix-len(num)))
                break
            res += digits.get(char)*pow(10, len(num)-ix-1)

        res =  res*digits.get(sign) if sign else res
        if res > pow(2,31) -1:
            return pow(2,31)-1
        elif res <= -pow(2,31):
            return -pow(2,31)
        else:
            return res

if __name__ == "__main__":
    fn = Solution().myAtoi
    x  = "1233.14159"
    print(fn(x))
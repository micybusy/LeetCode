class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9':9}

        def dnc(num_list):
            num = [nums.get(item) for item in num_list]
            num.reverse()
            num = sum([num[i]*(10**i) for i in range(len(num))])
            return num
        
        return str(dnc(num1)*dnc(num2))
        




if __name__ == "__main__":
    fn = Solution().multiply
    print(fn('2', '3'))
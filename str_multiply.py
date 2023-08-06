class Solution(object):
    def multiply(self, num1, num2):
        def intfy(num1):
            num_uno = 0
            for ix, digit in enumerate(num1):
                num_uno += (10**((len(num1)-ix -1)))*int(digit)
            return num_uno
        
        return str(intfy(num1)*intfy(num2))
    

if __name__ == '__main__':
    s = Solution()
    print(s.multiply('2', '3'))

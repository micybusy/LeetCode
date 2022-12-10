# done
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        generic = {1: [[1]], 2: [[1], [1, 1]]}
        if numRows in generic:
            return generic.get(numRows)
        
        rows = [[1], [1,1], [1, 2, 1]]
        for i in range(2, numRows-1):
            row = rows[i]
            combs = [[row[i], row[i+1]] for i in range(len(row)-1)]
            rows.append([1] + [sum(item) for item in combs] + [1])
        return rows



if __name__ == "__main__":
    fn = Solution().generate
    print(fn(2)) 
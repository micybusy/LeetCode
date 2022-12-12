class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = matrix[0].copy()
        row_len = len(spiral)
        col_len = len(matrix)
        flattened = [[item for item in sub] for sub in matrix]

        sign = 1
        for ix in range(row_len):
            try:
                spiral.append(flattened[sign*ix*col_len])
                flattened[ix*col_len] = "a"
            except:
                spiral.append(flattened[sign*ix*row_len])        
                flattened[ix*row_len] = "a"
            else:
                sign*=-1
        return spiral
        

    


if __name__ == "__main__":
    fn = Solution().spiralOrder
    inp = [[1,2,3],[4,5,6],[7,8,9]]
    print(fn(inp))
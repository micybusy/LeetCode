class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        side = len(matrix)
        matrix[:] = matrix[::-1]
        matrix[:] = [[item[i] for item in matrix] for i in range(side)]
        return matrix # returning not wanted in leetcode.



if __name__ == "__main__":
    fn = Solution().rotate
    x = [[1,2,3],[4,5,6],[7,8,9]]
    print(fn(x))



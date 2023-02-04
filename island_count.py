# not done :(
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    try:
                        up = grid[i+1][j]
                    except:
                        up = 0
                    try:
                        down = grid[i-1][j]
                    except:
                        down = 0
                    try:
                        left = grid[i][j+1]
                    except:
                        left = 0
                    try:
                        right = grid[i][j-1]
                    except:
                        right = 0
                    if (up, down, left, right) == (0, 0, 0, 0):
                        count+=1

        return count


if __name__ == "__main__":
    fn = Solution().numIslands
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ] # should return 1

    grid2 = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ] # should return 3

    print(fn(grid))
    print(fn(grid2))
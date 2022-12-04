class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        numeros = list(range(1, 10))
        numeros = [str(i) for i in numeros]
        cols = [[line[i] for line in board] for i in range(9)]
        first_col  = [line[0:3] for line in board]
        second_col = [line[3:6] for line in board]
        third_col  = [line[6:9] for line in board]
        subboxes   = [[item[0:3], item[3:6], item[6:9]] for item in [first_col, second_col, third_col]]

        flat_list = [item for sublist in subboxes for item in sublist]
        double_flat_list =  [item[0] + item[1] + item[2] for item in flat_list]
    
        if all([item.count(numero) <2 for item in board for numero in numeros]):
            if all([item.count(numero) <2 for item in cols for numero in numeros]):
                if all([item.count(numero)<2 for item in double_flat_list for numero in numeros]):
                    return True
        return False


if __name__ == '__main__':
    isv = Solution().isValidSudoku
    valid_board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
    print(isv(valid_board))

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowNums = collections.defaultdict(set)
        colNums = collections.defaultdict(set)
        squareNums = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowNums[i]:
                    return False
                if board[i][j] in colNums[j]:
                    return False
                if board[i][j] in squareNums[i//3, j//3]:
                    return False

                rowNums[i].add(board[i][j])
                colNums[j].add(board[i][j])
                squareNums[i//3, j//3].add(board[i][j])

        return True

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            rowNums = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowNums:
                    return False
                rowNums.add(board[i][j])

        for i in range(len(board)):
            colNums = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colNums:
                    return False
                colNums.add(board[j][i])

        squares = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in squares[(i//3, j//3)]:
                    return False
                squares[(i//3, j//3)].add(board[i][j])

        return True

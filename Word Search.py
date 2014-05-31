class Solution:
    def exist(self, board, word):
        visited = [[0 for y in range(len(board[0]))] for x in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecur(board, word, visited, i, j) == True:
                    return True
        return False
                
    def existRecur(self, board, word, visited, i, j):
        if len(word) == 0:
            return True
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or visited[i][j] == 1 or board[i][j] != word[0]:
            return False
        visited[i][j] = 1
        found = self.existRecur(board, word[1:], visited, i + 1, j) or self.existRecur(board, word[1:], visited, i - 1, j) or self.existRecur(board, word[1:], visited, i, j + 1) or self.existRecur(board, word[1:], visited, i, j - 1)
        visited[i][j] = 0
        return found
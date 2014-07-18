class Solution:
    def solve(self, board):
        if len(board) == 0:
            return
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        current = [(i, j) for i in range(len(board)) for j in (0, len(board[0]) - 1)] 
        current += [(i, j) for i in (0, len(board) - 1) for j in range(len(board[0]))]
        while current:
            i, j = current.pop()
            visited[i][j] = True
            if board[i][j] == 'O':
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] is False:
                        visited[x][y] = True
                        current.append((x, y))
        mapping = {'X': 'X', 'O': 'X', 'V': 'O'}
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = mapping[board[i][j]]

    def solve(self, board):
    """ Same code. I am not sure which version I like more.
	"""
        if len(board) == 0:
            return
        current, visited = [], [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            current.append((i, 0))
            current.append((i, len(board[0]) - 1))
        for i in range(len(board[0])):
            current.append((0, i))
            current.append((len(board) - 1, i))
        while current:
            i, j = current.pop()
            visited[i][j] = True
            if board[i][j] == 'O':
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] is False:
                        visited[x][y] = True
                        current.append((x, y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
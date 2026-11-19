class Game:
    def __init__(self, board):
        self.board = board
​
    def play(self):
        board = self.board
        n = len(board)
        seen = set()
        leaps = 0
​
        for i in range(n):
            for j in range(n):
                if board[i][j] and (i, j) not in seen:
                    leaps += 1
                    stack = [(i, j)]
                    seen.add((i, j))
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            a, b = x + dx, y + dy
                            if 0 <= a < n and 0 <= b < n and board[a][b] and (a, b) not in seen:
                                seen.add((a, b))
                                stack.append((a, b))
        return leaps
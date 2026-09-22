def passed_pawn(board):
    r, c = next((r, c) for r in range(8) for c in range(8) if board[r][c] == 'P')
    return not any(
        board[i][j] == 'p'
        for i in range(r)
        for j in range(max(0, c - 1), min(8, c + 2))
    )
from enum import Enum
​
class Piece(Enum):
    QUEEN = 'queen'
    ROOK = 'rook'
    BISHOP = 'bishop'
    KNIGHT = 'knight'
​
RULES = {
    Piece.QUEEN: lambda dr, dc: dr == 0 or dc == 0 or abs(dr) == abs(dc),
    Piece.ROOK: lambda dr, dc: dr == 0 or dc == 0,
    Piece.BISHOP: lambda dr, dc: abs(dr) == abs(dc),
    Piece.KNIGHT: lambda dr, dc: {abs(dr), abs(dc)} == {1, 2}
}
    
def promotion(board):
    pos = {v: (r, c) for r, row in enumerate(board)
                     for c, v in enumerate(row) if v in 'PK'}
    if 'P' not in pos or 'K' not in pos:
        return []
    dr, dc = pos['K'][0] - pos['P'][0], pos['K'][1] - pos['P'][1]
    return [p.value for p in Piece if RULES[p](dr, dc)]
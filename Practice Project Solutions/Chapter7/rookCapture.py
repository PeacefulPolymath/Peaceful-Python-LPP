def white_rook_can_capture(rook , board):
    captures = []
    for square , piece in board.items():
        if piece.lower().startswith('b'):
            if rook[0] == square[0] or rook[1] == square[1]:
                captures.append(square)
    return captures

print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))

board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


divider = "  -------------------------------"

# 'K' and 'k' for King, 'Q' and 'q' for Queen, etc.
# Uppercase letters for white pieces, lowercase for black
unicode_pieces = {
    'r': '\u265C', 'n': '\u265E', 'b': '\u265D', 'q': '\u265B', 'k': '\u265A', 'p': '\u265F',
    'R': '\u2656', 'N': '\u2658', 'B': '\u2657', 'Q': '\u2655', 'K': '\u2654', 'P': '\u2659',
    ' ': ' '
}

def print_board(board):
    print("Here's the board:")
    print(divider)
    num = 8
    for row in board:
        print(str(num) + "| {} | {} | {} | {} | {} | {} | {} | {} |".format(*row))
        print(divider)
        num -= 1
    print("   a   b   c   d   e   f   g   h")

print_board(board)
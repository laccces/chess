board = [['.' for _ in range(8)] for _ in range(8)]

divider = "  -------------------------------"

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
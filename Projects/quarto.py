def piece_str(piece):
    """Return a string representing the piece's properties."""
    if piece is None:
        return "    "
    # Properties: Tall/Short, Light/Dark, Square/Round, Solid/Hollow
    props = [
        "T" if piece & 8 else "S",  # Tall/Short
        "L" if piece & 4 else "D",  # Light/Dark
        "Q" if piece & 2 else "R",  # Square/Round
        "S" if piece & 1 else "H",  # Solid/Hollow
    ]
    return "".join(props)

def print_board(board):
    print("   0    1    2    3")
    for i, row in enumerate(board):
        print(i, end=" ")
        for piece in row:
            print(piece_str(piece), end=" ")
        print()

def check_win(board):
    # Check all rows, columns, and diagonals for a common property
    lines = []
    # Rows and columns
    for i in range(4):
        lines.append([board[i][j] for j in range(4)])
        lines.append([board[j][i] for j in range(4)])
    # Diagonals
    lines.append([board[i][i] for i in range(4)])
    lines.append([board[i][3-i] for i in range(4)])

    for line in lines:
        if None in line:
            continue
        for bit in range(4):
            if all(((piece >> bit) & 1) == ((line[0] >> bit) & 1) for piece in line):
                return True
    return False

def main():
    print("Quarto! (4x4)")
    print("Each piece is unique and has 4 properties.")
    print("On your turn, place the piece your opponent gave you, then pick a piece for your opponent.")
    print("First to make a line of 4 pieces sharing any property wins.\n")

    board = [[None for _ in range(4)] for _ in range(4)]
    available = set(range(16))
    turn = 0
    next_piece = None

    while True:
        print_board(board)
        print("Available pieces:", " ".join(f"{p}:{piece_str(p)}" for p in sorted(available)))
        player = "Player 1" if turn % 2 == 0 else "Player 2"

        # Place the piece chosen by the opponent
        if next_piece is not None:
            print(f"{player}, place piece {next_piece} ({piece_str(next_piece)})")
            while True:
                try:
                    pos = input("Enter row,col (e.g. 1,2): ")
                    row, col = map(int, pos.split(","))
                    if not (0 <= row < 4 and 0 <= col < 4):
                        print("Coordinates out of range.")
                        continue
                    if board[row][col] is not None:
                        print("Cell already taken.")
                        continue
                    board[row][col] = next_piece
                    available.remove(next_piece)
                    break
                except Exception:
                    print("Invalid input. Try again.")
            if check_win(board):
                print_board(board)
                print(f"{player} wins!")
                return
            if not available:
                print_board(board)
                print("Draw! No more pieces.")
                return

        # Choose a piece for the opponent
        print(f"{player}, choose a piece for your opponent to place next.")
        while True:
            try:
                chosen = int(input("Enter piece number: "))
                if chosen not in available:
                    print("Piece not available.")
                    continue
                next_piece = chosen
                break
            except Exception:
                print("Invalid input. Try again.")

        turn += 1

if __name__ == "__main__":
    main()
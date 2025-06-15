def print_board(board):
    print("  " + " ".join(str(i) for i in range(6)))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(cell if cell else "." for cell in row))

def check_win(board):
    # Check all rows, columns, and diagonals for five in a row (X or O)
    for symbol in ['X', 'O']:
        # Check rows
        for row in board:
            for i in range(2):
                if all(cell == symbol for cell in row[i:i+5]):
                    return True
        # Check columns
        for col in range(6):
            for i in range(2):
                if all(board[row][col] == symbol for row in range(i, i+5)):
                    return True
        # Check diagonals
        for i in range(2):
            for j in range(2):
                # Top-left to bottom-right
                if all(board[i+k][j+k] == symbol for k in range(5)):
                    return True
                # Top-right to bottom-left
                if all(board[i+k][j+4-k] == symbol for k in range(5)):
                    return True
    return False

def is_full(board):
    return all(all(cell for cell in row) for row in board)

def main():
    print("Order and Chaos (6x6)")
    print("Players take turns placing X or O anywhere on the board.")
    print("Order wins if there are five Xs or Os in a row, column, or diagonal.")
    print("Chaos wins if the board fills up without such a line.\n")

    board = [[None for _ in range(6)] for _ in range(6)]
    turn = 0  # Even: Order, Odd: Chaos

    while True:
        print_board(board)
        player = "Order" if turn % 2 == 0 else "Chaos"
        print(f"{player}'s turn.")
        while True:
            try:
                move = input("Enter row,col (e.g. 2,3): ")
                row, col = map(int, move.split(","))
                if not (0 <= row < 6 and 0 <= col < 6):
                    print("Coordinates out of range.")
                    continue
                if board[row][col]:
                    print("Cell already taken.")
                    continue
                symbol = input("Place X or O: ").upper()
                if symbol not in ("X", "O"):
                    print("Invalid symbol. Enter X or O.")
                    continue
                board[row][col] = symbol
                break
            except Exception:
                print("Invalid input. Try again.")

        if check_win(board):
            print_board(board)
            print("Order wins!")
            break
        if is_full(board):
            print_board(board)
            print("Chaos wins!")
            break
        turn += 1

if __name__ == "__main__":
    main()
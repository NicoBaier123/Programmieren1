class ChessBoard:
    def __init__(self):
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.current_player = 'white'  # Initialize the current player as white

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def display_board(self):
        root = tk.Tk()
        root.title("Chess Board")

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "white"
                    fg_color = "black"
                else:
                    color = "black"
                    fg_color = "white"

                piece = self.board[row][col]
                if piece == '-':
                    piece = ''

                if piece == 'P':
                    piece = '♙'
                elif piece == 'p':
                    piece = '♟'
                elif piece == 'K':
                    piece = '♔'  # Replace 'K' with '♔' for king
                elif piece == 'k':
                    piece = '♚'  # Replace 'k' with '♚' for king

                label = tk.Label(root, text=piece, width=4, height=2, relief="solid", bg=color, fg=fg_color)
                label.grid(row=row, column=col)

        root.mainloop()

    def switch_player(self):
        if self.current_player == 'white':
            self.current_player = 'black'
        else:
            self.current_player = 'white'

# Create a new chess board
board = ChessBoard()

# Place pieces for the first player (white)
board.place_piece('R', 0, 0)  # R represents a rook
board.place_piece('N', 0, 1)  # N represents a knight
board.place_piece('B', 0, 2)  # B represents a bishop
board.place_piece('Q', 0, 3)  # Q represents a queen
board.place_piece('K', 0, 4)  # K represents a king
board.place_piece('B', 0, 5)  # B represents a bishop
board.place_piece('N', 0, 6)  # N represents a knight
board.place_piece('R', 0, 7)  # R represents a rook

board.place_piece('♙', 1, 0)  # ♙ represents a pawn
board.place_piece('♙', 1, 1)  # ♙ represents a pawn
board.place_piece('♙', 1, 2)  # ♙ represents a pawn
board.place_piece('♙', 1, 3)  # ♙ represents a pawn
board.place_piece('♙', 1, 4)  # ♙ represents a pawn
board.place_piece('♙', 1, 5)  # ♙ represents a pawn
board.place_piece('♙', 1, 6)  # ♙ represents a pawn
board.place_piece('♙', 1, 7)  # ♙ represents a pawn

# Switch to the second player (black)
board.switch_player()

# Place pieces for the second player (black)
board.place_piece('r', 7, 0)  # r represents a rook
board.place_piece('n', 7, 1)  # n represents a knight
board.place_piece('b', 7, 2)  # b represents a bishop
board.place_piece('q', 7, 3)  # q represents a queen
board.place_piece('k', 7, 4)  # k represents a king
board.place_piece('b', 7, 5)  # b represents a bishop
board.place_piece('n', 7, 6)  # n represents a knight
board.place_piece('r', 7, 7)  # r represents a rook

board.place_piece('♟', 6, 0)  # ♟ represents a pawn
board.place_piece('♟', 6, 1)  # ♟ represents a pawn
board.place_piece('♟', 6, 2)  # ♟ represents a pawn
board.place_piece('♟', 6, 3)  # ♟ represents a pawn
board.place_piece('♟', 6, 4)  # ♟ represents a pawn
board.place_piece('♟', 6, 5)  # ♟ represents a pawn
board.place_piece('♟', 6, 6)  # ♟ represents a pawn
board.place_piece('♟', 6, 7)  # ♟ represents a pawn

# Display the chess board
board.display_board()

# Define the chess board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Function to print the chess board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to play the chess game
def play_chess():
    print("Welcome to Chess!")
    print_board(board)

    # Game loop
    while True:
        # Get user input for move
        move = input("Enter your move (e.g. e2 e4): ")
        from_pos, to_pos = move.split()

        # Convert positions to indices
        from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
        to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')

        # Make the move
        board[to_row][to_col] = board[from_row][from_col]
        board[from_row][from_col] = ' '

        # Print the updated board
        print_board(board)

# Start the game
play_chess()

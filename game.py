import random

global board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "x"
gameRunning = True
winner = None

def playerInput(board):
    pos = int(input("What spot on the board would you like to play? (1-9): "))
    if board[pos - 1] == "-":
        board[pos - 1] = currentPlayer
    elif board[pos - 1] != "-":
        print("Oops! That spot is already taken by a player. Try again.")
    else:
        print("Enter a valid number.")
        playerInput(board)
    printBoard

def printBoard(board):
    print(f"{board[0]}  |  {board[1]}  |  {board[2]}")
    print(f"{board[3]}  |  {board[4]}  |  {board[5]}")
    print(f"{board[6]}  |  {board[7]}  |  {board[8]}\n")

def computerPlay(board):
    pos = random.randint(0, 8)
    if board[pos] == "-":
        board[pos] = currentPlayer
    else:
        computerPlay()
    printBoard()


while gameRunning:
    printBoard(board)
    playerInput(board)
    computerPlay(board)

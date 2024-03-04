import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "x"
gameRunning = True
winner = None
player = "x"

def playerInput(board):
    try:
        pos = int(input("What spot on the board would you like to play? (1-9): "))
    except:
        print("Enter a valid number.")
        playerInput(board)
        
    if board[pos - 1] == "-":
        board[pos - 1] = currentPlayer
        printBoard(board)
        checkWin.checkWin(board)
        switchPlayer()

    elif board[pos - 1] != "-":
        print("Oops! That spot is already taken by a player. Try again.")
        playerInput(board)


def printBoard(board):
    print(f"{board[0]}  |  {board[1]}  |  {board[2]}")
    print(f"{board[3]}  |  {board[4]}  |  {board[5]}")
    print(f"{board[6]}  |  {board[7]}  |  {board[8]}\n")

def computerPlay(board):
    while currentPlayer != player:
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = currentPlayer
            print("Computer thinking: ...aha!")
            printBoard(board)
            checkWin.checkWin(board)
            switchPlayer()
        else:
            computerPlay(board)

def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

class checkWin:
    def checkTie(board):
        global gameRunning
        if "-" not in board:
            print("It's a draw!")
            gameRunning = False

    def checkRow(board):
        # if board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer or board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer or board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer:
        for i in range(0, 6, 3):
            if all(board[i + j] == currentPlayer for j in range(3)): 
                return True

    def checkColumn(board):
        for i in range(3):
            if all(board[i + j*3] == currentPlayer for j in range(3)): 
                return True
    
    def checkDiagonal(board):
        if (board[0] == board[4] == board[8] == currentPlayer) or \
           (board[2] == board[4] == board[6] == currentPlayer):
            return True
    
    def checkWin(board):
        global player
        global gameRunning
        if checkWin.checkRow(board) or checkWin.checkColumn(board) or checkWin.checkDiagonal(board):
            print(f"{currentPlayer.capitalize()} wins!")
            gameRunning = False
        elif checkWin.checkTie(board):
            if currentPlayer != player:
                print("Your turn now, dear human.")


printBoard(board)

while gameRunning:
    playerInput(board)
    if gameRunning:
        computerPlay(board)
        

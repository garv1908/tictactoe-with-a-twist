import random

board = {
    1: "-", 2: "-", 3: "-",
    4: "-", 5: "-", 6: "-",
    7: "-", 8: "-", 9: "-"
}

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
        
    if board[pos] == "-":
        board[pos] = currentPlayer
        printBoard(board)
        checkWin.checkWin(board)
        switchPlayer()

    elif board[pos] != "-":
        print("Oops! That spot is already taken by a player. Try again.")
        playerInput(board)


def printBoard(board):
    print(f"{board[1]}  |  {board[2]}  |  {board[3]}")
    print(f"{board[4]}  |  {board[5]}  |  {board[6]}")
    print(f"{board[7]}  |  {board[8]}  |  {board[9]}\n")

def computerPlay(board):
    while currentPlayer != player:
        pos = random.randint(1, 9)
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
        for i in range(1, 7, 3):
            if all(board[i + j] == currentPlayer for j in range(3)): 
                return True

    def checkColumn(board):
        for i in range(3):
            if all(board[i + j*3] == currentPlayer for j in range(3)): 
                return True
    
    def checkDiagonal(board):
        if (board[1] == board[5] == board[9] == currentPlayer) or \
           (board[3] == board[5] == board[7] == currentPlayer):
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
        

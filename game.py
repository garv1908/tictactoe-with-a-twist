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
opponent = "o"
global pos

def playerInput(board):
    try:
        pos = int(input("What spot on the board would you like to play? (1-9): "))
    except:
        print("Enter a valid number.")
        playerInput(board)
        
    if board[pos] == "-":
        board[pos] = currentPlayer
        printBoard(board)
        CheckWin.checkWin(board)
        switchPlayer()

    elif board[pos] != "-":
        print("Oops! That spot is already taken by a player. Try again.")
        playerInput(board)


def printBoard(board):
    print(f"{board[1]}  |  {board[2]}  |  {board[3]}")
    print(f"{board[4]}  |  {board[5]}  |  {board[6]}")
    print(f"{board[7]}  |  {board[8]}  |  {board[9]}\n")

class ComputerPlay:
    
    def __init__(self, board):
        self.board = board
        self.win = self.Win()

    """A player can play a perfect game of tic-tac-toe (to win or at least draw) if, each time it is their turn to play, they choose the first available move from the following list, as used in Newell and Simon's 1972 tic-tac-toe program.[19]

    Win: If the player has two in a row, they can place a third to get three in a row.
    Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
    Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it. Otherwise, the player should block all forks in any way that simultaneously allows them to make two in a row. Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in them producing a fork. For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win. (Playing a corner move in this scenario produces a fork for "X" to win.)
    Center: A player marks the center. (If it is the first move of the game, playing a corner move gives the second player more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
    Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    Empty corner: The player plays in a corner square.
    Empty side: The player plays in a middle square on any of the four sides.
            Source: Wikipedia"""
    class Win:
        def checkThree(x, y, z, who): # 'who' checks for either 'x' or 'o'
            global pos
            if ((((board[x] == who and board[y] == who) or (board[y] == who and board[z] == who) or (board[x] == who and board[z] == who)))\
                and ((board[x] == "-" or board[y] == "-" or board[z] == "-"))):
                empty_index = x if board[x] == "-" else (y if board[y] == "-" else z)
                pos = empty_index # sets pos to winning cell
        def winRow(XorO):
            for row in range(1, 8, 3):
                x = row
                y = row + 1
                z = row + 2
                ComputerPlay.Win.checkThree(x, y, z, XorO)

        def winCol(XorO):
            for column in range(1, 4):
                x = column
                y = column + 3
                z = column + 6
                ComputerPlay.Win.checkThree(x, y, z, XorO)

        def winDiag(XorO):
            # diagonal 1
            x, y, z = 1, 5, 9
            ComputerPlay.Win.checkThree(x, y, z, XorO)

            # diagonal2
            x, y, z = 3, 5, 7
            ComputerPlay.Win.checkThree(x, y, z, XorO)
        def play():
            computer = ComputerPlay(board).Win
            computer.winRow(currentPlayer)
            computer.winCol(currentPlayer)
            computer.winDiag(currentPlayer)
    class Block:
        def checkThree():
            global pos
            pos = -1
            computer = ComputerPlay.Win
            # below lines set pos variable to what is needed to play to block player
            computer.winRow(player)
            computer.winCol(player)
            computer.winDiag(player)
        def play():
            pass

    def play(self):
        global pos
        pos = -1
        while pos == -1:
            ComputerPlay.Win.play()
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay(board).Block.checkThree()
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay(board).playMove()

            
    def playMove(self):
        global pos
        if pos == -1 or board[pos] != "-":
            pos = random.randint(1, 9)
        if board[pos] == "-":
            board[pos] = currentPlayer
            print("Computer thinking: ...aha!")
            printBoard(board)
            CheckWin.checkWin(board)
            switchPlayer()
        else:
            ComputerPlay(board).playMove()

def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

class CheckWin:
    def checkTie(board):
        global gameRunning
        if all(board[i] != "-" for i in range(1,10)):
            return True

    def checkRow(board):
        # if board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer or board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer or board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer:
        for i in range(1, 8, 3):
            if all(board[i + j] == currentPlayer for j in range(3)): 
                return True

    def checkColumn(board):
        for i in range(1, 4):
            if all(board[i + j*3] == currentPlayer for j in range(3)): 
                return True
    
    def checkDiagonal(board):
        if (board[1] == board[5] == board[9] == currentPlayer) or \
           (board[3] == board[5] == board[7] == currentPlayer):
            return True
    
    def checkWin(board):
        global player
        global gameRunning
        if CheckWin.checkRow(board) or CheckWin.checkColumn(board) or CheckWin.checkDiagonal(board):
            print(f"{currentPlayer.capitalize()} wins!")
            gameRunning = False
        elif CheckWin.checkTie(board):
            print("It's a draw!")
            gameRunning = False
        elif currentPlayer != player:
                print("Your turn now, dear human.")


printBoard(board)

while gameRunning:
    playerInput(board)
    if gameRunning:
       ComputerPlay(board).play()
        
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
whoGoesFirst = "player"

global pos

global winCount
winCount = 0

"""
takes player input, with a validation check.
assigns move in array
checks for win
switches player
"""
def playerInput(board: dict):
    try:
        pos = int(input("What spot on the board would you like to play? (1-9): "))
        if board[pos] == "-":
            board[pos] = currentPlayer
            printBoard(board)
            CheckWin.checkWin(board)
            switchPlayer()
        elif board[pos] != "-":
            print("Oops! That spot is already taken by a player. Try again.")
            playerInput(board)
    except:
        print("Enter a valid number.")
        playerInput(board) # call recursively
        

"""
prints the board
"""
def printBoard(board):
    print(f"{board[1]}  |  {board[2]}  |  {board[3]}")
    print(f"{board[4]}  |  {board[5]}  |  {board[6]}")
    print(f"{board[7]}  |  {board[8]}  |  {board[9]}\n")

"""
class initalised with self 
"""
class ComputerPlay:
    
    def __init__(self, board):
        self.board = board
        self.win = self.Win()

    """A player can play a perfect game of tic-tac-toe (to win or at least draw) if, each time it is their turn to play, they choose the first available move from the following list, as used in Newell and Simon's 1972 tic-tac-toe program.[19]

    Win: If the player has two in a row, they can place a third to get three in a row.
    Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
    Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it.
        Otherwise, that simultaneously allows them to make two in a row.
        Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in them producing a fork.
            For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win.
            (Playing a corner move in this scenario produces a fork for "X" to win.)
    Center: A player marks the center. (If it is the first move of the game, playing a corner move gives the second player more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
    Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    Empty corner: The player plays in a corner square.
    Empty side: The player plays in a middle square on any of the four sides.
            Source: Wikipedia"""

    class Win:
        """
        checkThree takes in 3 positions x, y, z, and who -> who are we checking for
        the three positions are checked for a win, and sets pos to the empty cell, if found.
            if there's 2 cells with 'who', return position of empty cell
        # implementing new winCount variable for Fork functionality
        """
        def checkThree(x: int, y: int, z: int, who: str): # 'who' checks for either 'x' or 'o'
            global pos
            global winCount
            if ((((board[x] == who and board[y] == who) or (board[y] == who and board[z] == who) or (board[x] == who and board[z] == who)))\
                and ((board[x] == "-" or board[y] == "-" or board[z] == "-"))):
                # empty_index = x if board[x] == "-" else (y if board[y] == "-" else z)
                if board[x] == "-":
                    empty_index = x
                    winCount += 1
                elif board[y] == "-":
                    empty_index = y
                    winCount += 1
                else:
                    empty_index = z # z must be correct if others are false
                    winCount += 1
                pos = empty_index # sets pos to winning cell
        """
        checks each row for win
        """
        def winRow(XorO: str):
            for row in range(1, 8, 3):
                x = row
                y = row + 1
                z = row + 2
                ComputerPlay.Win.checkThree(x, y, z, XorO)

        """
        checks each column for win
        """
        def winCol(XorO: str):
            for column in range(1, 4): # column values: 1, 2, 3
                x = column
                y = column + 3
                z = column + 6
                ComputerPlay.Win.checkThree(x, y, z, XorO)
        
        """
        checks each diagonal for win
        """
        def winDiag(XorO: str):
            # diagonal 1
            x, y, z = 1, 5, 9
            ComputerPlay.Win.checkThree(x, y, z, XorO)

            # diagonal 2
            x, y, z = 3, 5, 7
            ComputerPlay.Win.checkThree(x, y, z, XorO)

        """
        checks each row, then each column, then each diagonal.
        as per checkThree, it assigns pos to the winning move if available
        """
        def play():
            computer = ComputerPlay(board).Win
            computer.winRow(currentPlayer)
            computer.winCol(currentPlayer)
            computer.winDiag(currentPlayer)

    """
    Block class contains play()
    """
    class Block:
        def play():
            global pos
            pos = -1
            computer = ComputerPlay.Win
            # below lines set pos variable to what is needed to play to block player
            # adapting code from ComputerPlay.Win class
            computer.winRow(player)
            computer.winCol(player)
            computer.winDiag(player)
            # can't use computer.play() as it doesn't take input for which player is passed

    """
    Fork class contains play()
    """
    class Fork:
        """
        sets cell to opponent XorO, checks for winCount with that play
        if winCount >= 2, position is stored and set at the end
        else, position stays at -1
        """
        def play():
            global winCount
            global pos
            global forceDefensePos # records all pos that allow a 2 in a row for computer
            forceDefensePos = set()
            forkIndex = -1
            for i in range(1, 10):
                winCount = 0 # reset winCount every iteration
                if board[i] == "-":
                    board[i] = opponent # replace cell with opponent variable
                    ComputerPlay.Win.play() # obtain new value for winCount
                    board[i] = "-" # reset replaced cell
                    if winCount >= 2:
                        forkIndex = i
                    elif winCount == 1:
                        forceDefensePos.add(i)
            pos = forkIndex

        """
        very similar to Fork.play()
        sets cell to player XorO, checks for winCount with that play
        if winCount >= 2, position is stored and set at the end
        else, position stays at -1
        """
        def blockPlay():
            global winCount
            global pos

            global forceDefesePos # records all pos that allow a 2 in a row for computer
            forkPos = set()
            
            blockForkIndex = -1
            
            for i in range(1, 10):
                winCount = 0 # reset winCount every iteration
                if board[i] == "-":
                    board[i] = player # replace cell with player variable
                    ComputerPlay.Block.play() # obtain new value for winCount
                    board[i] = "-" # reset replaced cell
                    if winCount >= 2:
                        blockForkIndex = i
                        forkPos.add(i)
                        pos = -1
                    elif winCount == 1: # means that the value of pos has changed due to Block.play()
                        pos = -1 # resets pos to -1 in case ComputerPlay.Block.play() changes its value

            numForks = len(forkPos)
            if numForks == 1:
                pos = blockForkIndex
            elif numForks > 1:
                """ play move that blocks fork and allows you to play 2 in a row """
                for i in forkPos:
                    board[i] = opponent # replace cell with opponent variable
                    ComputerPlay.Win.play() # sets pos to move that allows 2 in a row that coincides with elements in forkPos
                    if pos != -1: # looks for change in pos caused by Win.play(), if change is seen, record 'i' value which causes change
                        blockForkIndex = i
                    board[i] = "-" # reset replaced cell
                    pos = -1
                if blockForkIndex != -1:
                    pos = blockForkIndex
                else:
                    pos = -1 # reset pos if desired move is not found
                """ if no such move exists, force opponent into defending by playing 2 in a row, without the player being able to play a fork """
                if pos == -1 and forceDefensePos(0) != None:
                    print(forceDefensePos)
                    pos = forceDefensePos(0)
                    print("set pos from forceDefensePos move")

    """
    outlines the "ideal move" process taking place for the computer's move
    """
    def play(self):
        global pos
        pos = -1
        while pos == -1:
            ComputerPlay.Win.play()
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay(board).Block.play()
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay.Fork.play() # do I need to specify (board)?
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay.Fork.blockPlay()
            if pos != -1:
                ComputerPlay(board).playMove()
                break
            ComputerPlay(board).playMove()

    """
    playMove handles the actual mechanics of the computer playing a move
    direct function of the ComputerPlay class
    """
    def playMove(self):
        global pos
        if pos == -1 or board[pos] != "-":
            pos = random.randint(1, 9)
            print("didn't know what to play for perfection. generated random pos")
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
    if currentPlayer == player:
        currentPlayer = opponent
    else:
        currentPlayer = player

class CheckWin:
    def checkRow(board) -> bool:
        # if board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer or board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer or board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer:
        for i in range(1, 8, 3):
            if all(board[i + j] == currentPlayer for j in range(3)): 
                return True

    def checkColumn(board) -> bool:
        for i in range(1, 4):
            if all(board[i + j*3] == currentPlayer for j in range(3)): 
                return True
    
    def checkDiagonal(board) -> bool:
        if (board[1] == board[5] == board[9] == currentPlayer) or \
           (board[3] == board[5] == board[7] == currentPlayer):
            return True
    
    def checkTie(board) -> bool:
        global gameRunning
        if all(board[i] != "-" for i in range(1,10)):
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

def main():
    global player
    global opponent
    match whoGoesFirst:
        case "player":
            player = "x"
            opponent = "o"
            printBoard(board)
            while gameRunning:
                playerInput(board)
                if gameRunning:
                    ComputerPlay(board).play()
        case "computer":
            opponent = "x"
            player = "o"
            while gameRunning:
                ComputerPlay(board).play()
                if gameRunning:
                    playerInput(board)
            


            
if __name__ == "__main__":
    main()
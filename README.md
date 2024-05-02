# TicTacToe but you can't win!

## What exactly is this?

A tic-tac-toe game implementation that contains a 'try to LOSE' gamemode!
This is a fun twist on the classical tic-tac-toe, which is also included in the game. The player is allowed to choose whether the computer plays the _perfect_ game, or the perfect _imperfect_ game.

The main file to run is just [game.py](./game.py)! Hope you have some fun if you decide to try it out.

## More information:

This project has helped me understand how bigger program structures work. Even though this is probably not the example you would want to give for "perfect code", I'm grateful to acknowledge that I have still worked on and developed skills relating to similar matters.

The computer decides what move to play based on a list of steps outlined [here](en.wikipedia.org/wiki/Tic-tac-toe#Strategy). This list is used as a guideline by checking whether each condition is true or not, and if it is, then the computer plays the optimal move for that condition. I'm glad to have been able to also take a bit of a spin on the idea, which is honestly a very different change of pace for a _regular_ X's-and-O's/tic-tac-toe player like me. It's an ironic mode where you lose if you win, and win if you lose.

import random

 
 
def display_board(board):
    blankBoard="""

|-----------------|
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
""" 


def copy_board(board):
    blankBoard="""

|-----------------|
|     |     |     |
|     |     |     |
|-----------------|
|     |     |     |
|     |     |     |
|     |     |     |
|-----------------|
|     |     |     |
|     |     |     |
|     |     |     |
|-----------------|
"""






 
 
def FirstTurn():
	if random.randint(0, 1) == 0:
	 return 'computer'
	else:
	 return 'player'
	   
def draw(playerLetter):
	

	print('   |   |')
	
	print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
	
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
	print('   |   |\n\n')
	print('-----------\n')
	print('Above diagram represents the setup of game')
	print("Select from 1-9 as shown in the figure and '" + playerLetter + "' will be  placed on that position\n\n")
	

def TheBoardDraw(board):

 	
    print('   |   |')
	
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')


def inputLetterForPlayer():

    # Lets the player type which letter they want to be.

    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
 letter = ''
 d = 0
 while not (letter == 'X' or letter == 'O'):
  if d != 0:
   print("Letter typed is neither 'X' nor 'O'")
  print('Do you want to be X or O?')
  d += 1
  letter = input().upper()



     # the first element in the list is the player’s letter, the second is the computer's letter.

 if letter == 'X':
  return ['X', 'O']

 else:
  return ['O', 'X']
  
 






def playTheGameAgain():

     # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')

    return input().lower().startswith('y')

 
def DoAMove(board, letter, move):
	board[move] = letter

def WinnerIsFinally(board, mark):
 	

     # Given a board and a player’s letter, this function returns True if that player has won.

     # We use bo instead of board and le instead of letter so we don’t have to type as much.

    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False



def CopyTheBoardDone(board):

     # Make a duplicate of the board list and return it the duplicate.
 dupeBoard = []

 for i in board:
  dupeBoard.append(i)



 return dupeBoard



def IfSpaceIsFree(board, move):

      # Return true if the passed move is free on the passed board.

	return board[move] == ' '

 

def getPlayerMove(board):

     # Let the player type in their move.
 move = ' '
 c = 0

 while move not in '1 2 3 4 5 6 7 8 9'.split() or not IfSpaceIsFree(board, int(move)):
  
  if ( c != 0 ):
   print("Input given is either not in 1-9 or the box is already filled")
  print('What is your move? (1-9)') 
  move = input()
  
  c += 1
   
 return int(move)



def chooseRandomMoveFromList(board, movesList):
     # Returns a valid move from the passed list on the passed board.

      # Returns None if there is no valid move.

    possibleMoves = []

    for i in movesList:

        if IfSpaceIsFree(board, i):

            possibleMoves.append(i)
        
            



    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)

    else:

        return None

 
def getComputerMove(board, computerLetter):

     # Given a board and the computer's letter, determine where to move and return that move.

    if computerLetter == 'X':

        playerLetter = 'O'
    else:

        playerLetter = 'X'



     # Here is our algorithm for our Tic Tac Toe AI:

     # First, check if we can win in the next move

    for i in range(1, 10):

        copy = CopyTheBoardDone(board)

        if IfSpaceIsFree(copy, i):

            DoAMove(copy, computerLetter, i)

            if WinnerIsFinally(copy, computerLetter):

                return i



     # Check if the player could win on their next move, and block them.

    for i in range(1, 10):

        copy = CopyTheBoardDone(board)

        if IfSpaceIsFree(copy, i):

            DoAMove(copy, playerLetter, i)

            if WinnerIsFinally(copy, playerLetter):

                return i



     # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    if move != None:

        return move



     # Try to take the center, if it is free.

    if IfSpaceIsFree(board, 5):

        return 5



     # Move on one of the sides.

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])



def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, 10):

        if IfSpaceIsFree(board, i):

            return False

    return True





print('Welcome to Tic Tac Toe!')


while True:

     # Reset the board

    theBoard = [' '] * 10
    display_board(theBoard)
    copy_board(theBoard)
    playerLetter, computerLetter = inputLetterForPlayer()
    print("You have chosen " + playerLetter)
    print("Hence computer has chosen " + computerLetter)
    turn = FirstTurn()
    
    gameIsPlaying = True
    tree = 'true'		

    if tree == 'true':
    		
    	draw(playerLetter)
    	tree = 'false'
    print('The ' + turn + ' will go first.')		

    while gameIsPlaying:
    	
    	#if tree == 'true':
    		
    	#	draw()
    	#	tree = 'false'
    		
	
        if turn == 'player':
            
             # Player’s turn.
	    	
            TheBoardDraw(theBoard)

            move = getPlayerMove(theBoard)

            DoAMove(theBoard, playerLetter, move)



            if WinnerIsFinally(theBoard, playerLetter):

                TheBoardDraw(theBoard)

                print('Hooray! You have won the game!')

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    TheBoardDraw(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'computer'



        else:

             # Computer’s turn.

            move = getComputerMove(theBoard, computerLetter)
            print("Computer places '" + computerLetter + "' at " + str(move))
            DoAMove(theBoard, computerLetter, move)
	    


            if WinnerIsFinally(theBoard, computerLetter):

                TheBoardDraw(theBoard)

                print('The computer has beaten you! You lose.')

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    TheBoardDraw(theBoard)

                    print('The game is a tie!')

                    break

                else:
                    turn = 'player'
    if not playTheGameAgain():
        break

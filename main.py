##Tic Tac Toe
#Name: John Nguyen
#Date: Fed 10

#1. (Var) Setup the empty board as a list
theBoard = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
exampleBoard = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none
def printBoard(board):
    print(' ', board[7], ' | ', board[8], ' | ', board[9])
    print('------------------')
    print(' ', board[4], ' | ', board[5], ' | ', board[6])
    print('------------------')
    print(' ', board[1], ' | ', board[2], ' | ', board[3])

printBoard (exampleBoard)

#3a. (fun) Determine if player is X or O
player1 = ' '
player2 = ' '

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None
def chooseLetter(letter):
    global player1
    global player2
    if letter == 'X' :
        player1 = 'X'
        player2 = 'O'
    else :
        player1 = 'O'
        player2 = 'X'


#3b. (fun) Choose starting player 1 or 2
def chooseStart(start):
    pass


#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none
def playerMove(board, case, player):
    board[case] = player


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
def checkWin(board, player):
    #Horizontal check :
    if board[1] == player and board[2] == player and board[3] == player:
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        return True
    #Vertical check :
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        return True
    #Cross check :
    elif board[1] == player and board[5] == player and board[9] == player:
        return True
    elif board[3] == player and board[5] == player and board[7] == player:
        return True
    #The game continue
    else:
        return False


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise
def checkFull(board):
    if board.count(' ') == 0 :
        return True
    else:
        return False


#7. Main function
print ()
print ('Type main() ')

def main():
    global player1
    global player2

    #print Welcome
    print ('Welcome to Tic Tac Toe!')
    print ()
    #print instructions
    print ('Please follow these instructions :')
    print ('1. Player move are between 1 and 9.')
    print ('  This is example board :')
    printBoard (exampleBoard)
    print ('2. Player 1 will go first')
    print ()
    #game play

    #get player letter choice
    letterChoice = input ('Choose your letter : ')
    chooseLetter (letterChoice)

    #while board is not full
    while checkFull (theBoard) == False :
        ###first player move
        case = int(input('Player 1 move : '))
        #player chooses move
        playerMove (theBoard, case, player1)
        #print board
        printBoard (theBoard)
        #check win :
        if checkWin (theBoard, player1) == True :
            print ('Player 1 win!!!!')
            print ('The End')
            break
        #check board full
        checkFull (theBoard)
        if checkFull (theBoard) == True :
            break

        ###second player move
        case = int(input('Player 2 move : '))
        #player chooses move
        playerMove (theBoard, case, player2)
        #choose again :
        printBoard (theBoard)
        #check win :
        if checkWin (theBoard, player2) == True :
            print ('Player 2 win!!!!')
            print ('The End')
            break
        #check board full
        checkFull (theBoard)
        if checkFull (theBoard) == True :
            print('The End')
            break


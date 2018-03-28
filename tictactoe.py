board = [' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' '] #declaration of board
legend = ['9', '|', '8', '|', '7', '6', '|', '5', '|', '4', '3', '|', '2', '|', '1'] # of legend
movehistory=[] #log of the moves executed
def DrawLegend(): #drawing the board
    print (legend[0] + legend[1] + legend[2] + legend[3] + legend[4])
    print ('------')
    print (legend[5] + legend[6] + legend[7] + legend[8] + legend[9])
    print ('------')
    print (legend[10] + legend[11] + legend [12] + legend [13] + legend[14])

def draw(): #drawing the board
    print ('Board: \n')
    print (board[0] + board[1] + board[2] + board[3] + board[4])
    print ('------')
    print (board[5] + board[6] + board[7] + board[8] + board[9])
    print ('------')
    print (board[10] + board[11] + board [12] + board [13] + board[14])

def moves1(): #player 1's moves
    print ('What is your move player 1? ')
    moves1.move = int(input())
    while moves1.move > 9 or moves1.move < 0:
        print ('\n Invalid move \n')
        moves1()
    for number in movehistory:
        if number == moves1.move:
            print ('Sorry that move has already been done \n')
            moves1()

def moves2(): #player 2's moves
    print ('What is your move player 2? ')
    moves2.move = int(input())
    while moves2.move > 9 or moves2.move < 0:
            print ('\n Invalid move \n')
            moves2()
    for number in movehistory:
        if number == moves2.move:
            print ('Sorry that move has already been done \n')
            moves2()
    
def ChangingBoard1(): #when player 1 causing a change in board
    if picking.letter == 'x':
        if moves1.move == 1:
            board[14] = 'X'
            draw()
        if moves1.move == 2:
            board[12] = 'X'
            draw()
        if moves1.move == 3:
            board[10] = 'X'
            draw()
        if moves1.move == 4:
            board[9] = 'X'
            draw()
        if moves1.move == 5:
            board[7] = 'X'
            draw()
        if moves1.move == 6:
            board[5] = 'X'
            draw()
        if moves1.move == 7:
            board[4] = 'X'
            draw()
        if moves1.move == 8:
            board[2] = 'X'
            draw()
        if moves1.move == 9:
            board[0] = 'X'
            draw()
    if picking.letter == 'o':
        if moves1.move == 1:
            board[14] = 'O'
            draw()
        if moves1.move == 2:
            board[12] = 'O'
            draw()
        if moves1.move == 3:
            board[10] = 'O'
            draw()
        if moves1.move == 4:
            board[9] = 'O'
            draw()
        if moves1.move == 5:
            board[7] = 'O'
            draw()
        if moves1.move == 6:
            board[5] = 'O'
            draw()
        if moves1.move == 7:
            board[4] = 'O'
            draw()
        if moves1.move == 8:
            board[2] = 'O'
            draw()
        if moves1.move == 9:
            board[0] = 'O'
            draw()
    
            
def ChangingBoard2(): #player 2 making a change in the board
    if picking.letter == 'o':
        if moves2.move == 1:
            board[14] = 'X'
            draw()
        if moves2.move == 2:
            board[12] = 'X'
            draw()
        if moves2.move == 3:
            board[10] = 'X'
            draw()
        if moves2.move == 4:
            board[9] = 'X'
            draw()
        if moves2.move == 5:
            board[7] = 'X'
            draw()
        if moves2.move == 6:
            board[5] = 'X'
            draw()
        if moves2.move == 7:
            board[4] = 'X'
            draw()
        if moves2.move == 8:
            board[2] = 'X'
            draw()
        if moves2.move == 9:
            board[0] = 'X'
            draw()
    if picking.letter == 'x':
        if moves2.move == 1:
            board[14] = 'O'
            draw()
        if moves2.move == 2:
            board[12] = 'O'
            draw()
        if moves2.move == 3:
            board[10] = 'O'
            draw()
        if moves2.move == 4:
            board[9] = 'O'
            draw()
        if moves2.move == 5:
            board[7] = 'O'
            draw()
        if moves2.move == 6:
            board[5] = 'O'
            draw()
        if moves2.move == 7:
            board[4] = 'O'
            draw()
        if moves2.move == 8:
            board[2] = 'O'
            draw()
        if moves2.move == 9:
            board[0] = 'O'
            draw()
        


def check(): #stating which letters each player will be
    if picking.letter == 'x':
        print ('Okay ' + player2, 'that means you are O')
    if picking.letter == 'o':
        print ('Okay ' + player2, 'that means you are X')

def picking():
    print ('Do want to be X or O ' + player1, '? \n')
    picking.letter = input()
    if picking.letter == 'o' or picking.letter == 'x':
        check()
    else:
        print('Invalid letter! \n')
        picking()


def winner(): #how to determine a winner
    if all(x == 'X' for x in (board[0], board[2], board[4])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[0], board[5], board[10])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[0], board[7], board[14])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[10], board[12], board[14])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[7], board[2], board[12])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[14], board[9], board[4])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[5], board[7], board[9])):
        print(' Congrats you won!')
        return True
    if all(x == 'X' for x in (board[10], board[7], board[4])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[0], board[2], board[4])): #starting at O
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[0], board[5], board[10])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[0], board[7], board[14])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[10], board[12], board[14])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[7], board[2], board[12])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[14], board[9], board[4])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[5], board[7], board[9])):
        print(' Congrats you won!')
        return True
    if all(x == 'O' for x in (board[10], board[7], board[4])):
        print(' Congrats you won!')
        return True
    else:
        return False
        
def game1(): #sequence of game
    moves1()
    movehistory.append(moves1.move)
    ChangingBoard1()
    print ('\n')
    DrawLegend()

def game2(): #sequence for player 2
    moves2()
    movehistory.append(moves2.move)
    ChangingBoard2()
    print ('\n')
    DrawLegend()
    
#beginning the game
print ('Hello who is player 1?')
player1= input()
print ('And player 2?')
player2= input()
print ('Okay let us get started! \n')
picking()

#initialization
draw()
print('\n')
print('Legend: \n')
DrawLegend()
count = 0

#checking if someone has won or not
def IsWinner():
    while winner() is False:
        count=count + 1
        game1()
        if winner() is True:
            break
        count=count + 1
        if count > 9:
            print ('Cats game! \n')
            break
        game2()
        if winner() is True:
            break




#when the board tile is changed the entire thing is changed, meaning we actually change it in the global... 
#actually playing







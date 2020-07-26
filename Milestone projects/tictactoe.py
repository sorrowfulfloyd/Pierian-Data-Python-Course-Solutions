nextTurn = 0 # 1 for X, 2 for O
gMoveInput = None
gUserMove = None
gOccupied = None

# gB.update({str(moveInput): userMove.upper()})

gB = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def betturPlayaSelector():
    digitMove = 0
    while True:
        inp = input("X or O?:\n> ")
        if inp not in ['X', 'x', 'O', 'o']:
            print('Only accept X or O.')
            continue
        if inp.upper() == 'X':
            digitMove = 1
            break
        elif inp.upper() == 'O':
            digitMove = 2
            break
        else:
            print('Unknown error')
            break
    return digitMove

# To check the play
def moveInputFromUser():
    global gB
    moveInput = ''
    while True:
        try:
            moveInput = int(input("Choose where to put your piece (1-9):\n> "))
            if (int(moveInput) not in [1,2,3,4,5,6,7,8,9]):
                print("Enter a cell between 1-9!")
                continue
            if gB[int(moveInput)] in ['X', 'O']:
                print("That cell is already occupied!")
                continue
            else:
                break
        except:
            print("Invalid Input Please try again")
    return moveInput

def usersMove():
    global nextTurn
    while True:
        if int(nextTurn) == 1:
            gB[int(gMoveInput)] = 'X'
            nextTurn = 2
            break
        else:
            gB[int(gMoveInput)] = 'O'
            nextTurn = 1
            break

# Function to draw to board after every move
def drawScreen():
        return(('' + gB[7] + '|' + gB[8] + '|' + gB[9] + '' + '\n'
        + "-----------" + '\n'
        + '' + gB[4] + '|' + gB[5] + '|' + gB[6] + '' + '\n'
        + "-----------" + '\n'
        + '' + gB[1] + '|' + gB[2] + '|' + gB[3] + '' + '\n'))

def win_check():
    global gB
    if gB[1] == 'X' and gB[2] == 'X' and gB[3] == 'X':
        return True
    if gB[4] == 'X' and gB[5] == 'X' and gB[6] == 'X':
        return True
    if gB[7] == 'X' and gB[8] == 'X' and gB[9] == 'X':
        return True
    if gB[7] == 'X' and gB[4] == 'X' and gB[1] == 'X':
        return True
    if gB[8] == 'X' and gB[5] == 'X' and gB[2] == 'X':
        return True
    if gB[9] == 'X' and gB[6] == 'X' and gB[3] == 'X':
        return True
    if gB[7] == 'X' and gB[5] == 'X' and gB[3] == 'X':
        return True
    if gB[1] == 'X' and gB[5] == 'X' and gB[9] == 'X':
        return True
    if gB[1] == 'O' and gB[2] == 'O' and gB[3] == 'O':
        return False
    if gB[4] == 'O' and gB[5] == 'O' and gB[6] == 'O':
        return False
    if gB[7] == 'O' and gB[8] == 'O' and gB[9] == 'O':
        return False
    if gB[7] == 'O' and gB[4] == 'O' and gB[1] == 'O':
        return False
    if gB[8] == 'O' and gB[5] == 'O' and gB[2] == 'O':
        return False
    if gB[9] == 'O' and gB[6] == 'O' and gB[3] == 'O':
        return False
    if gB[7] == 'O' and gB[5] == 'O' and gB[3] == 'O':
        return False
    if gB[1] == 'O' and gB[5] == 'O' and gB[9] == 'O':
        return False

def playAgain():
    imp = input('Game over do you wanna play again? y or n\n> ')
    while True:
        if imp.lower() not in ['y', 'n']:
            print('y for yes, n for no please.')
            continue
        if imp.lower() == 'y':
            return True
        elif imp.lower() == 'n':
            return False

print("Welcome to YATG")


while True:
    if int(nextTurn) < 1:
        nextTurn = betturPlayaSelector()
    else:
        pass
    gMoveInput = str(moveInputFromUser())
    usersMove()
    print(drawScreen())
    if win_check() == True or win_check() == False:
        if playAgain() == False:
            print('Thanks for playing!')
            break
        if playAgain() == True:
            nextTurn == 0
            nextTurn = betturPlayaSelector()
            gB = ['#','','','','','','','','','']
            continue

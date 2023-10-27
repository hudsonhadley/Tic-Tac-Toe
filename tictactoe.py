# A program that plays tic tac toe in the command line
# The AI is made using the minimax algorithm and alpha beta pruning
# Although it does not need pruning, but it is a nice example
# By Hudson Hadley

import random

# prints board
def printBoard(a):
    print('{}|{}|{}'.format(a[0], a[1], a[2]))
    print('-----')
    print('{}|{}|{}'.format(a[3], a[4], a[5]))
    print('-----')
    print('{}|{}|{}\n\n'.format(a[6], a[7], a[8]))


def instructions():
    print('1|2|3')
    print('-----')
    print('4|5|6')
    print('-----')
    print('7|8|9\n\n')


# returns 'X' if X has won
# returns 'O' if O has won
def testBoard(a):
    b = ['X', 'O']

    # 0|1|2
    # -----
    # 3|4|5
    # -----
    # 6|7|8

    # go through all the win situations with X and O
    for k in b:
        # top row
        if a[0] == k and a[1] == k and a[2] == k:
            return k

        # middle row
        elif a[3] == k and a[4] == k and a[5] == k:
            return k

        # bottom row
        elif a[6] == k and a[7] == k and a[8] == k:
            return k

        # first column
        elif a[0] == k and a[3] == k and a[6] == k:
            return k

        # second column
        elif a[1] == k and a[4] == k and a[7] == k:
            return k

        # third column
        elif a[2] == k and a[5] == k and a[8] == k:
            return k

        # top left to bottom right diagonal
        elif a[0] == k and a[4] == k and a[8] == k:
            return k

        # top right to bottom left diagonal
        elif a[2] == k and a[4] == k and a[6] == k:
            return k

    # if there's an open spot
    try:
        if a[openSpots(a)[0] - 1] == ' ':
            return 0

    # if there's a tie
    except:
        return 'Tie'


def openSpots(a):
    o = []

    for i in range(1, 10):
        if a[i - 1] == ' ':
            o.append(i)

    return o



# our terrible AI
def badAI(a, p):
    return random.choice(openSpots(a))



# just blocks or wins or picks a random open spot
def goodAI(a, p):
    other = nextTurn(p)

    copyBoard = a

    if 5 in openSpots(a):
        return 5

    marks = [p, other]

    for k in marks:
        for i in openSpots(copyBoard):
            copyBoard[i - 1] = k

            if testBoard(copyBoard) == k:
                return i

            copyBoard[i - 1] = ' '

    return random.choice(openSpots(a))




# gets user input
def user(a, p):
    c = 0

    while c not in openSpots(a):
        try:
            c = int(input())

        except:
            pass

    return c


def play(t, a):
    if t == 'O':
        # badAI / goodAI / user
        p = user(a, t)
        a[p - 1] = 'O'

    if t == 'X':
        # goodAI / badAI / perfectAI / user
        p = perfectAI(a, t)
        a[p - 1] = 'X'

    return a


# The perfect AI works by going through each
# possible move it can do and evaluating which
# is best using the minimax algorithm
def perfectAI(a, t):
    biggest = -100

    for i in openSpots(a):
        a[i - 1] = t
        current = minimax(a, False, nextTurn(t))
        a[i - 1] = ' '

        if current > biggest:
            biggest = current
            bestMove = i

    return bestMove


# Our algorithm to decide which move is best by going
# through each move and board that it can do and if X
# wins a 1 is returned. If O wins -1 is returned. If it
# is a tie a 0 is returned
def minimax(a, isMaximizing, t):

    if isMaximizing:

        scores = {
            t : 1,
            nextTurn(t) : -1,
            'Tie': 0
        }

    else:

        scores = {
            nextTurn(t) : 1,
            t : -1,
            'Tie' : 0
        }

    # If the game is over just return who won
    if testBoard(board) != 0:
        return scores[testBoard(a)]

    # If it is the maximizing player's turn
    if isMaximizing:
        biggest = -100

        # For every open spot
        for i in openSpots(a):
            # Play
            a[i - 1] = t
            # Evaluate it
            current = minimax(a, False, nextTurn(t))
            # Unplay it
            a[i - 1] = ' '

            # If its a better score than the best than make it the best
            biggest = max(biggest, current)

        return biggest


    else:
        smallest = 100

        for i in openSpots(a):
            a[i - 1] = t
            current = minimax(a, True, nextTurn(t))
            a[i - 1] = ' '

            smallest = min(smallest, current)

        return smallest


def nextTurn(t):
    if t == 'X':
        return 'O'

    else:
        return 'X'



board = [' '] * 9
turn = random.choice(['X', 'O'])

while testBoard(board) == 0:
    instructions()
    printBoard(board)

    print('{}\'s turn\n'.format(turn))
    board = play(turn, board)

    turn = nextTurn(turn)

instructions()
printBoard(board)

if testBoard(board) == 'Tie':
    print('Tie!')

else:
    print('{} wins!'.format(testBoard(board)))
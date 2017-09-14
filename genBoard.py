import random

def board_setup():
    ships = [('D',2), ('S', 3), ('R', 3), ('B',4), ('C',5) ]
    w = h = 10
    board = [['_' for x in range(w)]  for y in range(h)]
    for ship in ships:
        not_placed = True
        while(not_placed):
            orien = random.randrange(0,2)
            if orien == 1:
                xr = random.randrange(0, w-ship[1])
                yr = random.randrange(0,h)
                flag = True
                for i in range(ship[1]):
                    if board[xr + i][yr] != '_':
                        flag = False
                if flag == True:
                    for i in range(ship[1]):
                        board[xr +i][yr] = ship[0]
                    not_placed = False
            else:
                xr = random.randrange(0,w)
                yr = random.randrange(0, h-ship[1])
                flag = True
                for i in range(ship[1]):
                    if board[xr][yr + i] != '_':
                        flag = False
                if flag == True:
                    for i in range(ship[1]):
                        board[xr][yr+i] = ship[0]
                    not_placed = False;
        #end while
    #END FOR
    return board

def save_board(board, file_name):
    with open(file_name, "w") as f:
        for line in board:
            str = "".join(line)
            print(str)
            f.write("".join(line) + "\n")

import sys

board = board_setup()

save_board(board, sys.argv[1])

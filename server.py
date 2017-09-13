import random
from flask import Flask, render_template, Response, request

ships = [('D',2), ('S', 3), ('R', 3), ('B',4), ('C',5) ]

def board_setup():
    w, h = 10
    board = [['_' for x in range(w)]  for y in range(h)]
    for ship in ships:
        not_placed = True
        while(not_placed):
            orien = random.uniform(0,1)
            if orien == 1:
                xr = random.uniform(0, w-ship)
                yr = random.uniform(0,h)
                flag = True
                for i in range(ship[1]):
                    if board[xr + i][yr] != '_':
                        flag = False
                if flag == True:
                    for i in range(ship[1]):
                        board[xr +i][yr] = ship[0]
                    not_placed = False
            else:
                xr = random.uniform(0,w)
                yr = random.uniform(0, h-ship)
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

def showHTML():
    doStuff()

#fired upon
#/fire?x=5&y=4
@app.route('/fire', methods = ['POST'])
def update_own_board():
    x = request.args.get('x')
    y = request.args.get('y')
    print("x = %s, y = %s" % x , y)
    
    # if out of bounds?
    if x >= 10 or y >= 10 or x < 0 or y < 0:
        return make_response("Out of bounds", 404)
    # spot has already been fired on
    elif board[x][y] == 'H' or board[x][y] == 'M':
        return make_response("Already fired on this spot", 410)
    # they missed the dang thing:
    elif board[x][y] == '_':
        board[x][y] = 'M'
        save_board(board, "board.txt")
        return make_response("hit=0", 200)
    # they hit:
    else:
        old = board[x][y]
        board[x][y] = 'H'
        save_board(board, "board.txt")
        numb = count_occurences(old, board)
        if numb == 0:
            # we sunk
            return make_response("hit=1&sink=%s" % old, 200)
        else:
            return make_response("hit=1", 200)
        
def count_occurences(to_count, board):
    count = 0
    for line in board:
        count = count + line.count(to_count)
    return count
        
#fired at
#/response?info=H&sink=D&x=4&y=5
@app.route('/response', methods = ['POST'])
def update_opponent_board():
    # is the hit/miss mark
    info = request.args.get('info')
    # is the ship that was sunk, or 0
    sink = request.args.get('sink')
    
    x = request.args.get('x')
    y = request.args.get('y')

    board = read_board("opponent_board.txt")
    
    # no error checking!
    if sink != 0:
        board[x][y] = sink
    else:
        board[x][y] = info
    
    save_board(board, "opponent_board.txt")
    return make_response("Board updated", 200)


def save_board(board, file_name):
    with open(file_name, "w") as f:
        for line in board:
            f.write(line)
    
def read_board(file_name):
    F = open(file_name, "r")
    board = []
    for line in F:
        board.append(line)
    F.close()
    return board


def doStuff():
    print("Not implemented yet")

doStuff()



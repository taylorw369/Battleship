import random
import sys
from flask import Flask, render_template, Response, request, make_response, send_from_directory

app = Flask(__name__)

port = sys.argv[1]
own_board = sys.argv[2]

def save_board(board, file_name):
    with open(file_name, "w") as f:
        for line in board:
            f.write("".join(line) + "\n")

def read_board(file_name):
    board = []
    with open(file_name, "r") as f:
        print(f)
        for line in f:
            board.append(list(line.rstrip(' \n')))
    return board

# # Hacky hacky hacky!
@app.route('/<path:path>')
def showHTML(path):
     return render_template(path, board=read_board()


#fired upon
#/fire?x=5&y=4
@app.route('/fire', methods = ['POST'])
def update_own_board():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))

    board = read_board(own_board)

    print("x = %d, y = %d" % (x, y))
    # if out of bounds?
    if x >= 10 or y >= 10 or x < 0 or y < 0:
        return make_response("Out of bounds\n", 404)
    # spot has already been fired on
    elif board[y][x] == 'H' or board[y][x] == 'M':
        return make_response("Already fired on this spot\n", 410)
    # they missed the dang thing:
    elif board[y][x] == '_':
        board[y][x] = 'M'
        save_board(board, own_board)
        return make_response("hit=0", 200)
    # they hit:
    else:
        old = board[y][x]
        board[y][x] = 'H'
        save_board(board, own_board)
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
        board[y][x] = sink
    else:
        board[y][x] = info

    save_board(board, "opponent_board.txt")
    return make_response("Board updated", 200)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')

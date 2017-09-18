import requests
import sys

opponent_board = "opponent_board.txt"

def save_board(board, file_name):
    with open(file_name, "w") as f:
        for line in board:
            f.write("".join(line) + "\n")

def read_board(file_name):
    board = []
    try:
        with open(file_name, "r") as f:
            print(f)
            for line in f:
                board.append(list(line.rstrip(' \n')))
            return board
    except FileNotFoundError:
        return None


def fire(ip, port, x, y):
    r = requests.post("http://" + ip + ":" + port + "/fire?x=" + x + "&y=" + y)
    print("text:  " + r.text)
    print("status: %d" % (r.status_code))

    if r.status_code == 404:
        print("coordinates are out of bounds")
    elif r.status_code == 410:
        print("coordinates have already been fired upon")
    elif r.status_code == 400:
        print("your message was formatted incorrectly")
    elif r.status_code == 200:
        print("good job, mate, you formatted it correctly")
        codes = get_codes(r.text)
        # variables
        hit = 0
        info = ""
        sink = "0"
        # load the opponent's board:
        op_board = read_board(opponent_board)
        
        if not op_board:
            op_board = []
            for i in range(0,10):
                op_board[i] = "__________"
        
        
        if "hit" in codes:
            if codes["hit"] == "1":
                print("You hit!") #put in the ship that was sunk
                if "sink" in codes:
                    print("you sunk: %s" % (codes["sink"]))
                    board[y][x] = codes["sink"]
                else:
                    board[y][x] = "H"
            else:
                board[y][x] = "M"
                print("you missed")
            # don't forget to save the board!
            save_board(op_board, opponent_board)
        else:
            print("Return message not formatted correctly")



def get_codes(message_text):
    to_return = dict()
    vals = message_text.split("&")
    for item in vals:
        sub = item.split("=")
        to_return[sub[0]] = sub[1]
    return to_return


if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    x = sys.argv[3]
    y = sys.argv[4]
    fire(ip, port, x, y)

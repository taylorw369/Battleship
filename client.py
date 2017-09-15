import requests
import sys

ip = sys.argv[1]
port = sys.argv[2]
x = sys.argv[3]
y = sys.argv[4]

def fire():

    payload = {'x': x, 'y': y}
    r = requests.post("http://" + ip + ":" + port, data=payload)
    print("text:  " + r.text)
    print("/nstatus: " + r.status_code)

    if r.status_code == 404:
        print("coordinates are out of bounds")
    elif r.status_code == 410:
        print("coordinates have already been fired upon")
    elif r.status_code == 400:
        print("your message was formatted incorrectly")
    elif r.status_code == 200:
        print("good job, mate")
        codes = get_codes(r.text)
        # variables
        hit = 0
        info = ""
        sink = 0
        if "hit" in codes:
            print("You hit!") #put in the ship that was sunk
            hit = 1
            if "sunk" in codes:
                print("you sunk: %s" % (codes["sunk"]))
                sink = 1
                info = code["sunk"]
            else:
                info = "H"
        else:
            info = "M"



def get_codes(message_text):
    to_return = dict()
    vals = message_text.split("&")
    for item in vals:
        sub = item.split("=")
        to_return[sub[0]] = sub[1]
    return to_return


if __name__ == "__main__":
    fire()

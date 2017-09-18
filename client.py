import requests
import sys

ip = sys.argv[1]
port = sys.argv[2]
x = sys.argv[3]
y = sys.argv[4]

def fire():


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
        if "hit" in codes:
            if codes["hit"] == "1":
                print("You hit!") #put in the ship that was sunk
                hit = 1
                if "sink" in codes:
                    print("you sunk: %s" % (codes["sink"]))
                    sink = codes["sink"] 
                    info = "H"
                else:
                    info = "H"
            else:
                info = "M"
                print("you missed")
        requests.post("http://127.0.0.1:" + port + "/response?info=" + info + "&sink=" + sink + "&x=" + x + "&y=" + y)



def get_codes(message_text):
    to_return = dict()
    vals = message_text.split("&")
    for item in vals:
        sub = item.split("=")
        to_return[sub[0]] = sub[1]
    return to_return


if __name__ == "__main__":
    fire()

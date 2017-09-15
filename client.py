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
        if int(codes[0]) == 1 and codes.length >1
            print("You sunk ") #put in the ship that was sunk
            if codes

def get_codes(message_text):
    to_return = []
    vals = message_text.split("&")
    for item in vals:
        to_return.append(item.split("=")[1])
    return to_return
    

if __name__ == "__main__":
    fire()
    

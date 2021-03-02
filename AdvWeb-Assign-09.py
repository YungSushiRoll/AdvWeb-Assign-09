import requests
import json
import datetime
import random
from gpiozero import Button
from time import sleep

def log():
    # get current date / time
    t = datetime.datetime.now()
    # format date in json format for RESTful API
    filename = "{0}-{1}-{2}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d")) + ".log"
    t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
    print(t_json + " Here 1")
    print(filename)
    # get random int for location
    rand = random.randint(1,3)
    print(rand)
    # create a new event - replace with your API
    url = 'https://modas-jsg.azurewebsites.net/api/event/'
    headers = { 'Content-Type': 'application/json'}
    payload = { 'timestamp': t_json, 'flagged': False, 'locationId': rand }
    # post the event
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(r.status_code)
    print(r.json())
    f = open(filename, "a")
    f.write(t_json + ",False,"+str(rand)+","+str(r.status_code)+ "\n")
    f.close()
    
# init button
button = Button(8)
button.when_released = log

try:
    # program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
    print("goodbye")

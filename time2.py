import time
from datetime import datetime

dnow = datetime.now()

timer_over = False




#time needs to be in seconds, not minutes
def timer(timea):
    global timer_over
    a_time = int(datetime.now().strftime("%S"))

    while True:
        b_time = int(datetime.now().strftime("%S"))

        timediff = (b_time - a_time) % 60

        if timediff == timea:
            timer_over = True
            break
        if timediff == -3:
            timer_over = False

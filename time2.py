import time
from datetime import datetime

time.time()

dnow = datetime.now()

timer_over = False

def five_sec_timer():

    a_time = int(datetime.now().strftime("%S"))

    while True:
        b_time = int(datetime.now().strftime("%S"))

        timediff = (b_time - a_time) % 60

        if timediff == 5:
            print("It's been 5 seconds")
            break

        time.sleep(1)


#time needs to be 00 format, not 0. And for now, should be under 61 seconds cuz i don't feel like figuring that out rn.
def timer(timea):
    global timer_over
    a_time = int(datetime.now().strftime("%S"))

    while True:
        b_time = int(datetime.now().strftime("%S"))

        timediff = (b_time - a_time) % 60

        if timediff == timea:
            timer_over = True
            print("Done")
            break




timer(10)

print(timer_over)

seconds = 00
minutes = 00
hours = 1

import time

from turtle import *
setup()
t1 = Turtle()


while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ("Comic Sans MS", 30, "bold"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1

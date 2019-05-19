from controller import quad
import time
q = quad.QuadCenter()
time.sleep(1)
speed = 750
while True:
    q.start(speed)
    inp = input()
    if inp == "a":
        speed +=10
    elif inp == "d":
        speed -= 10
    elif inp == "s":
        speed = 0
        break





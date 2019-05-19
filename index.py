from controller import quad
import time
q = quad.QuadCenter()
time.sleep(1)
speed = 750
print("start with 750")
input("Wait to inter")
q.start(speed)
while True:
    q.increase(q.dc1,speed)
    q.increase(q.dc2, speed)
    q.increase(q.dc3, speed)
    q.increase(q.dc4, speed)
    print("change speed:"+speed)
    inp = input()
    if inp == "a":
        speed +=10
    elif inp == "d":
        speed -= 10
    elif inp == "s":
        speed = 0
        break





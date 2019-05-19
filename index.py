from controller import quad
import time
q = quad.QuadCenter()
time.sleep(1)
speed = 750
max_value = 2000
q.start(0)
input("Please dis connect and enter")
q.start(max_value)
input("Please connect battery with two beep and enter")
q.start(speed)
time.sleep(7)
print( "Wait for it ....")
time.sleep(5)
print("Im working on it, DONT WORRY JUST WAIT.....")
q.start(0)
time.sleep(2)
print( "Arming ESC now...")
q.start(speed)
time.sleep(1)
print( "I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
time.sleep(1)

while True:
    q.increase(q.dc1,speed)
    q.increase(q.dc2, speed)
    q.increase(q.dc3, speed)
    q.increase(q.dc4, speed)
    print("change speed:%d", speed)
    inp = input()
    if inp == "a":
        speed +=10
    elif inp == "d":
        speed -= 10
    elif inp == "s":
        speed = 0
        break





import RPi.GPIO as GPIO

import time

import logging


logging.basicConfig()
log = logging.getLogger('websocket')
log.setLevel(logging.INFO)


GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

dc1 = GPIO.PWM(7,50)
dc2 = GPIO.PWM(11,50)
dc3 = GPIO.PWM(13,50)
dc4 = GPIO.PWM(15,50)
dc1.start(0)
dc2.start(0)
dc3.start(0)
dc4.start(0)


dc1.ChangeDutyCycle(0)
dc2.ChangeDutyCycle(0)
dc3.ChangeDutyCycle(0)
dc4.ChangeDutyCycle(0)



log.info("Start calibration")
time.sleep(3)
dc1.ChangeDutyCycle(0)
dc2.ChangeDutyCycle(0)
dc3.ChangeDutyCycle(0)
dc4.ChangeDutyCycle(0)

log.info("Disconnect the battery and press Enter")
ip = input()


dc1.ChangeDutyCycle(100)
dc2.ChangeDutyCycle(100)
dc3.ChangeDutyCycle(100)
dc4.ChangeDutyCycle(100)

log.info("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
ip = input()
dc1.ChangeDutyCycle(1)
dc2.ChangeDutyCycle(1)
dc3.ChangeDutyCycle(1)
dc4.ChangeDutyCycle(1)

time.sleep(12)
dc1.ChangeDutyCycle(0)
dc2.ChangeDutyCycle(0)
dc3.ChangeDutyCycle(0)
dc4.ChangeDutyCycle(0)

time.sleep(2)
dc1.ChangeDutyCycle(1)
dc2.ChangeDutyCycle(1)
dc3.ChangeDutyCycle(1)
dc4.ChangeDutyCycle(1)

time.sleep(1)

log.info("done")

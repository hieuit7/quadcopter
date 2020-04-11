#!/usr/bin/env python3

# WS server example that synchronizes state across clients
import time
import RPi.GPIO as GPIO
import asyncio
import json
import logging
import websockets

logging.basicConfig()
log = logging.getLogger('websocket')
log.setLevel(logging.INFO)

clients = set()


class Serve:
    def __init__(self, websocket):
        self.websocket = websocket
        GPIO.setmode(GPIO.BOARD)

        GPIO.setwarnings(False)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

        self.t1 = GPIO.PWM(7, 50)
        self.t2 = GPIO.PWM(11, 50)
        self.t3 = GPIO.PWM(13, 50)
        self.t4 = GPIO.PWM(15, 50)

        self.t1.start(0)
        self.t2.start(0)
        self.t3.start(0)
        self.t4.start(0)
        # time.sleep(10)

        self.change_speed(0)
        time.sleep(3)

    def change_speed(self, speed):
        self.t1.ChangeDutyCycle(speed)
        self.t2.ChangeDutyCycle(speed)
        self.t3.ChangeDutyCycle(speed)
        self.t4.ChangeDutyCycle(speed)

    def calibrate(self):
        self.change_speed(0)
        log.info("Disconnected ")
        self.change_speed(15)
        log.info(
            "Connect battery now!! you will here two beeps, then wait for a gradual falling tone then press Enter")

        self.change_speed(1)
        log.info("Wierd eh! Special tone")
        time.sleep(7)
        log.info("Wait for it ....")
        time.sleep(5)
        log.info("Im working on it, DONT WORRY JUST WAIT.....")
        self.change_speed(0)
        time.sleep(2)
        log.info("Arming ESC now...")
        self.change_speed(1)
        time.sleep(1)
        log.info("See.... uhhhhh")


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


async def consumer(serve, message):
    # process event with brushless
    cy = 0;
    try:
        if message.startswith('c'):
            serve.calibrate()
        else:
            cycle = float(message)
            input_cycle = translate(abs(cycle), 0, 150, 0, 10)
            cy = input_cycle
            serve.change_speed(input_cycle)
            log.info("mess", input_cycle)
    except Exception as e:
        log.info("send number", e, message, cy)


async def consumer_handler(websocket, path):
    serve = Serve(websocket)
    async for message in websocket:
        await consumer(serve, message)


async def listen(websocket, path):
    clients.add(websocket)
    # await asyncio.wait([websocket.send('ss')])
    consumer_task = asyncio.ensure_future(
        consumer_handler(websocket, path))
    done, pending = await asyncio.wait(
        [consumer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()


start_server = websockets.serve(listen, "0.0.0.0", 6789)
log.info("listening 6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

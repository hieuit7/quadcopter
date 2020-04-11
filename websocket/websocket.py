#!/usr/bin/env python3

# WS server example that synchronizes state across clients
import time
import RPi.GPIO as GPIO
import asyncio
import json
import logging
import websockets
logging.basicConfig()
clients = set()

class Serve:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setwarnings(True)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)

        self.t1 = GPIO.PWM(7, 50)
        self.t2 = GPIO.PWM(11, 50)
        # t2 = GPIO.PWM(7, 50)
        # t2 = GPIO.PWM(7, 50)

        self.t1.start(0)
        self.t2.start(0)
        # time.sleep(10)

        self.t1.ChangeDutyCycle(3)
        self.t2.ChangeDutyCycle(3)
        time.sleep(3)

    def change_speed(self, speed):
        self.t1.ChangeDutyCycle(speed)
        self.t2.ChangeDutyCycle(speed)


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)



async def consumer(serve, message):
    #process event with brushless
    cy = 0;
    try:
        cycle = float(message)

        input_cycle = translate(abs(cycle),0,150,0,10)
        cy = input_cycle
        serve.change_speed(input_cycle)
        print("mess",input_cycle)
    except Exception as e:
        print("send number", e, message, cy)

async def consumer_handler(websocket, path):
    serve = Serve()

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
print("listening 6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
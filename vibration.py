import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
import servo

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    global word
    if GPIO.input(channel):
        t1 = Thread(target=servo.emoteWalk)
        t2 = Thread(target=servo.emoteShakeHead)
        t1.start()
        t2.start()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500)
GPIO.add_event_callback(channel, callback)

while True:
    sleep(1)
    print(GPIO.input(channel))
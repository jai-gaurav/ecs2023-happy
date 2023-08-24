import time
import RPi.GPIO as GPIO

touch_pin1 = 13
touch_pin2 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(touch_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def touch_det(pin):
    touch=GPIO.input(pin)
    return touch

while True:
    if (touch_det(touch_pin1) or touch_det(touch_pin2)): 
        print('['+time.ctime()+'] - '+'Touch Detected')
    time.sleep(0.2)
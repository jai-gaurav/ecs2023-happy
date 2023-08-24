import time
import RPi.GPIO as GPIO

touch_pin1 = 13           # pin for left side sensor 
touch_pin2 = 19           # pin for right side sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(touch_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def touch_det(pin):
    touch=GPIO.input(pin)
    return touch

def isTouchingLeft():
    if touch_det(touch_pin1):
        return True
    else:
        return False

def isTouchingRight():
    if touch_det(touch_pin2):
        return True
    else:
        return False



### testing touch.py file
while True:
    if (touch_det(touch_pin1) or touch_det(touch_pin2)): 
        print('['+time.ctime()+'] - '+'Touch Detected')
    time.sleep(0.2)


### testing junk functions
# from random import choices
# def isTouchingLeft():
#     return choices((0,1), (100,1))[0]

# def isTouchingRight():
#     return choices((0,1), (100,1))[0]
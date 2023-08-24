# import necessary libraries
from adafruit_servokit import ServoKit
from time import sleep


# set environment variables
kit = ServoKit(channels=16)


# change channel values as per connection of servos to pca9685
channel_lhand = 1
channel_rhand = 0
channel_head = 2


# initialize all servos to default value (center at 90)
kit.servo[channel_head].angle = 90
kit.servo[channel_lhand].angle = 90
kit.servo[channel_rhand].angle = 90



### helper function for returning to default position
def emoteDefault():
    kit.servo[channel_lhand].angle = 90
    kit.servo[channel_rhand].angle = 90
    kit.servo[channel_head].angle = 90

### helper function for walking emote
def emoteWalk():
    emoteDefault()
    for i in range(3):
        sleep(0.35)
        kit.servo[channel_lhand].angle = 0
        kit.servo[channel_rhand].angle = 0
        sleep(0.35)
        kit.servo[channel_lhand].angle = 180
        kit.servo[channel_rhand].angle = 180
    sleep(0.35)
    kit.servo[channel_lhand].angle = 0
    kit.servo[channel_rhand].angle = 0
    sleep(0.3)
    emoteDefault()

### helper function for waving with right hand
def emoteWaveR():
    emoteDefault()
    for i in range(4):
        sleep(0.3)
        kit.servo[channel_rhand].angle = 180
        sleep(0.3)
        kit.servo[channel_rhand].angle = 120
    sleep(0.3)
    emoteDefault()

### helper function for waving with left hand
def emoteWaveL():
    emoteDefault()
    for i in range(4):
        sleep(0.3)
        kit.servo[channel_lhand].angle = 0
        sleep(0.3)
        kit.servo[channel_lhand].angle = 60
    sleep(0.3)
    emoteDefault()

### helper function for pointing forward with right hand
def emotePointR():
    emoteDefault()
    sleep(0.3)
    kit.servo[channel_rhand].angle = 180

### helper function for pointing forward with left hand
def emotePointL():
    emoteDefault()
    sleep(0.3)
    kit.servo[channel_lhand].angle = 0

### helper function for party dance
def emoteParty():
    emoteDefault()
    for i in range(5):
        sleep(0.3)
        kit.servo[channel_lhand].angle = 0
        kit.servo[channel_rhand].angle = 180
        sleep(0.3)
        kit.servo[channel_lhand].angle = 30
        kit.servo[channel_rhand].angle = 150
    sleep(0.3)
    emoteDefault()

### helper function to look right
def emoteLookRight():
    emoteDefault()
    sleep(0.3)
    kit.servo[channel_head].angle = 0
    sleep(2.5)
    emoteDefault()

### helper function to look left
def emoteLookLeft():
    emoteDefault()
    sleep(0.3)
    kit.servo[channel_head].angle = 180
    sleep(2.5)
    emoteDefault()

### helper function to shake head no
def emoteShakeHead():
    emoteDefault()
    sleep(0.1)
    for i in range(3):
        sleep(0.3)
        kit.servo[channel_head].angle = 120
        sleep(0.3)
        kit.servo[channel_head].angle = 60
    sleep(0.4)
    emoteDefault()



# testing code
emoteDefault()
print("letsgo")
while True:
    sleep(2)
    emotePointL()
    sleep(2)
    emotePointR()
    sleep(2)
    emoteWaveL()
    sleep(2)
    emoteWaveR()
    sleep(2)
    emoteWalk()
    sleep(2)
    emoteParty()
    sleep(2)
    emoteLookLeft()
    sleep(2)
    emoteLookRight()
    sleep(2)
    emoteShakeHead()
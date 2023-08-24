import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

def emoteHi(hand = 'left'):
    if hand == 'left':
        channel = 7
    elif hand == 'right':
        channel = 0

    kit.servo[channel].angle = 180
    print(kit.servo[channel].angle)
    kit.servo[channel].angle = 0
    print(kit.servo[channel].angle)
    time.sleep(0.3)
    kit.servo[channel].angle = 90
    print(kit.servo[channel].angle)
    time.sleep(0.2)
    kit.servo[channel].angle = 0
    print(kit.servo[channel].angle)
    time.sleep(0.2)
    kit.servo[channel].angle = 90
    print(kit.servo[channel].angle)
    time.sleep(0.2)
    kit.servo[channel].angle = 0
    print(kit.servo[channel].angle)
    time.sleep(0.2)
    kit.servo[channel].angle = 180
    print(kit.servo[channel].angle)

"""
while True:
    action = input("Enter 0 for moving left hand, 1 for right, 2 for both: ")

    if action == '0':
        emoteHi('left')
    elif action == '1':
        emoteHi('right')
    elif action == '2':
        emoteHi('left')
        emoteHi('right')
"""

kit.servo[7].set_pulse_width_range(100, 2750)
kit.servo[7].actuation_range = 180

"""
for i in range(150,-1,-10):
    kit.servo[7].angle = i
    time.sleep(1)
    print(kit.servo[7].angle)
"""


kit.servo[7].angle = 14
time.sleep(2)
kit.servo[7].angle = 140

# # get setup
# import time
# print("Ready to go!")
# curPos = 0

# # function to move right hand
# def moveRightHand(pos=0):
#     for i in range(4):
#         print("Moving rght hand")
#         time.sleep(0.5)

#     print("Moved right hand by", pos, "units")

# # function to move left hand
# def moveLeftHand(pos=0):
#     print("Moved left hand by", pos, "units")



# import necessary libraries
import time
import Adafruit_PCA9685

# initialize PCA9685 using default address (0x40)
pwm = Adafruit_PCA9685.PCA9685()

# configure min and max servo pulse lengths (out of 4096)
servo_min = 150 
servo_max = 600

# helper function to make setting servo pulse width simpler
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000              # 1000000 us per second
    pulse_length //= 60                 # for 60Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096               # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *=  1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# set frequency to 60Hz which is good for servos
pwm.set_pwm_frequency(60)

print("Moving servo on channel 0")
while True:
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
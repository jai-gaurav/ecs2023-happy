import hands
import random
import time

while True:
    io = random.randint(1, 4)

    if (io == 0):
        break
    elif (io == 1):
        hands.moveRightHand(30)
    elif (io == 2):
        hands.moveLeftHand(30)
    elif (io == 3):
        # do something
        print("Nothing changed")
    elif (io == 4):
        # do something
        print("Nothing changed")

    time.sleep(1)
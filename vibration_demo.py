from threading import Thread
from servo import emoteShakeHead, emoteWalk


t1 = Thread(target=emoteShakeHead)
t2 = Thread(target=emoteWalk)
t1.start()
t2.start()
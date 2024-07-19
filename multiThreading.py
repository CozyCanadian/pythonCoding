import threading
import time

def threadFunction():
    print("timeA")
    time.sleep(5)
    print("timeB")

timeThread = threading.Thread(target=threadFunction)
timeThread.start()

print("another time")
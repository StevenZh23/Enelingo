#Class to update energy usage and reset at end of week
#imports
from datetime import datetime, timedelta
import time
import threading


# instance data
currTime = time.localtime()
timeToReset = 0 # both in seconds
currentDay = datetime.today()
for i in range(0,6):
    if (i + currentDay.weekday() == 6):
        timeToReset = (6 - i) * 24 * 60 * 60


# method to update time
def updateTime():
    global timeToReset
    time.sleep(60)
    timeToReset -= 60

def start_timer_in_background():
    timer_thread = threading.Thread(target=updateTime, args=(60,))
    timer_thread.daemon = True  # Ensures thread exits when the main program ends
    timer_thread.start()

#method to reset time
def reset():
    while(timeToReset > 0):
        start_timer_in_background()
    timeToReset = 7 * 24 * 60 * 60    
    

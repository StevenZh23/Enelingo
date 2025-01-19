#Class to update energy usage and reset at end of week
#imports
from datetime import datetime, timedelta
import time

# instance data
currentDay
currTime = time.localtime()
resetTime # both in seconds
currentDay = datetime.today()
for i in range(0,6):
    if (i + currentDay.weekday() == 6):
        resetTime = (6 - i) * 24 * 60 * 60


# method to update time
def updateTime():
    currTime.sleep(60)
    resetTime-= currTime

#method to reset time
def reset():
    while(resetTime > 0):
        updateTime()
    resetTime = 7 * 24 * 60 * 60    
    



    

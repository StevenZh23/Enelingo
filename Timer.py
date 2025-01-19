#Class to update energy usage and reset at end of week
#imports

from datetime import datetime, timedelta
import time
import threading
from PersonalDatabase import spend_energy, reset_spent # Assuming this is defined in your module



def calculate_seconds_to_next_week():
    now = datetime.now()

    day = (now.weekday() if now.weekday() != 6 else -1)
    next_sunday = now + timedelta(days=(6 - day))

    next_sunday_start = datetime.combine(next_sunday, datetime.min.time())


    return int((next_sunday_start - now).total_seconds())

# Function to update energy usage at regular intervals
def update_energy_in_background(user, stop_event):
    interval = 60  # Update every 60 seconds
    time_to_reset = calculate_seconds_to_next_week()

    while not stop_event.is_set():
        # Spend energy for the user
        spend_energy(user)
        #print(time_to_reset)
        # Decrease time-to-reset and check if it's time to reset
        time.sleep(interval)
        time_to_reset -= interval

        if time_to_reset <= 0:
            reset_spent(user)
            time_to_reset = calculate_seconds_to_next_week()  # Recalculate for the next week

# Start the background timer
def start_background_timer(user):
    stop_event = threading.Event()  # Event to signal the thread to stop
    timer_thread = threading.Thread(target=update_energy_in_background, args=(user, stop_event))
    timer_thread.daemon = True  # Ensure the thread stops when the main program exits
    timer_thread.start()
    return stop_event

# Example usage
#user = "binky"  # Replace with your user logic
#stop_event = start_background_timer(user)

    # Simulate running the main app
#try:
#    while True:
#        time.sleep(1)  # Keep the main program running
#except KeyboardInterrupt:
#    print("Stopping the timer...")
#    stop_event.set()  # Signal the timer thread to stop


'''
# instance data
currTime = time.localtime()
timeToReset = 0 # both in seconds
currentDay = datetime.today()
for i in range(0,6):
    if (i + currentDay.weekday() == 6):
        timeToReset = (6 - i) * 24 * 60 * 60


# method to update time
def updateTime(user):
    global timeToReset
    spend_energy(user)
    time.sleep(60)
    timeToReset -= 60
    #print(timeToReset)

def start_timer_in_background(user):
    timer_thread = threading.Thread(target=updateTime, args=(user,))
    #timer_thread.daemon = True  # Ensures thread exits when the main program ends
    timer_thread.start()

#method to reset time
def reset(user):
    global timeToReset
    while timeToReset > 0:
        updateTime(user)

    timeToReset = 7 * 24 * 60 * 60    

#print(timeToReset)
#start_timer_in_background("binky")
#print(timeToReset)

'''
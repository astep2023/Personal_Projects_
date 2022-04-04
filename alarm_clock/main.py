import time
import winsound
import threading
import signal
import sys
from datetime import datetime
#-----------------------------------#
#GLOBAL VARIABLES
running = True

#-----------------------------------#
#This section is meant to display the time. I have it checking to see if countdown is still alive and if it is, then it'll do something. I honestly can't remember what tf I was thinking when I started that, but that is how it is for now. I'll probably go ahead and change it later cause looking back at it after not for a few days, that shit looks wack.

def signal_handler(sig, frame):
    global running
    running = False
    print('You pressed Ctrl+C!')
#-----------------------------------#
def display_time():    
    global running
    while running:
        date_time = datetime.now().strftime("%H:%M:%S")
        print(date_time)
        time.sleep(1)
#-----------------------------------#
def countdown(seconds):
    global a_clock
    global running
    while running:
        while seconds >= 0:
            seconds -= 1
            time.sleep(1)
        print("Done")
        #winsound.Beep(3000, 1000)
        a_clock.time_set()
#-----------------------------------#
class alarm_clock():
    def __init__(self):
        self.time_set()
    
    def time_set(self):
        try: 
            self.seconds = int(input("How many seconds: "))
        except:
            sys.exit(0)
    # This run method honestly looks terrible. I hate it. But this was like the messy and brute way I got things to display. Pretty sure the try and except stuff can be removed and this run method can be cut down a lot and the work can be put in other methods most likely.

    # So realized the try and except is actually still needed. The try and except is there to not recreate a thread_display thread. So a new thread isn't created each time you make a new timer/count_down.
    def run(self):
        if self.seconds <= -1:
            sys.exit(0)
        else:
            while self.seconds >= 0:
                thread_countdown = threading.Thread(target=countdown, args=(self.seconds,))
                thread_display = threading.Thread(target=display_time)
                thread_countdown.start()
                thread_display.start()
                thread_countdown.join()
                thread_display.join()

#-----------------------------------#
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    a_clock = alarm_clock()
    a_clock.run()

#-----------------------------------#

#This section below is just the original. It can be ignored overall.

#def countdown(seconds):
    #while seconds:
    #    time.sleep(1)
   #     seconds -=1
  #  winsound.Beep(3000, 1000)
 #   print("Done")

#def get_user_input_time():
   # time = int(input("Enter seconds before alarm: "))
   # return time


#if __name__ == "__main__":
 #   input_time = get_user_input_time()
  #  countdown(input_time)
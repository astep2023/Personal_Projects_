from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime
from queue import PriorityQueue
alarms = PriorityQueue()
alarms.put((1, "Hello"))
alarms.put((2, "Goodbye"))


def time(current, next):
            string = strftime("%H:%M:%S")
            first = alarms.queue[0][1]
            current.config(text = string)
            current.after(1000, time())
            next.config(text = first)
            next.after(1000, time()) 

class main_display(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x200")
        self.title("Alarm Clock")
        #Creating display labels.
        current_time_label = Label(self, font = ('calibri', 20, 'bold'),
            background = '#4180c4', foreground = 'white', text = "Current Time", justify = LEFT, width = 10).grid(row = 0, column = 0, padx = 10, ipadx = 10)
        current_time = Label(self, borderwidth= 40, font = ('calibri', 20, 'bold'), foreground = 'darkred', relief = "sunken", background = "darkgrey", justify = LEFT)
        next_alarm_label = Label(self, font = ('calibri', 20, 'bold'),
            background = '#4180c4', foreground = 'white', text = "Next Alarm", width = 10).grid(row = 2, column = 0, padx = 10, ipadx = 10)
        next_alarm = Label(self, borderwidth = 2, font = ('calibri', 20, 'bold'), foreground = 'darkred', relief = "sunken", background = "darkgrey")


        add_button = Button(self, text = "Add")
        #add_button.configure(command = lambda: add_alarm_display())
        alarms_button = Button(self, text = "List Alarms")
        #alarms_button.configure(command=lambda: list_alarms())
        snooze_button = Button(self, text = "Snooze")
        #snooze_button.configure(command = lambda: snooze_alarm())
        off_button = Button(self, text = "Off")
        #off_button.configure(command=lambda: stop_alarm())

        #Placing all the objects.
        current_time.grid(row = 1, column = 0, padx = 10, pady = 10, 
                    ipadx = 10)
        next_alarm.grid(row = 3, column = 0, padx = 10, pady = 10, 
                    ipadx = 10)
        add_button.place(x = 250, y = 20)
        alarms_button.place(x = 250, y = 40)
        snooze_button.place(x = 250, y = 60)
        off_button.place(x = 250, y = 80)
        

def main():
    app = main_display()
    print(help(Frame()))
    app.mainloop()

if __name__ == "__main__":
    main()
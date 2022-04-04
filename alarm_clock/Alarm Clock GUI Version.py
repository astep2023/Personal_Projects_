from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime
from queue import PriorityQueue

alarms = PriorityQueue()
alarms.put((1, "Hello"))
alarms.put((2, "Goodbye"))

clock_window = Tk()
clock_window.geometry('350x200')
clock_window.title('Alarm Clock')

def list_alarms():
    alarm_window = Tk()
    for i in range(len(alarms.queue)):
        temp_time = alarms.queue[i][1]
        temp_label = Label(alarm_window, text=str(temp_time))
        temp_label.pack()
    

def stop_alarm():
    pass

def snooze_alarm():
    alarms.queue[0]

def add_alarm_display():
    def add_alarm(hour, minute, second):
        hour = hour_.get()
        minute = minute_.get()
        second = second_.get()
        alarm = "{} {} {}".format(hour, minute, second)
        alarms.put(((len(alarms.queue) + 1), alarm))

    add_window = Tk()
    add_window.title('Add Alarm')
    add_window.geometry('400x300')
    add_window.config(bg='#F2B90C')

    hours_array = [i for i in range(60)]

    # setting hour_ for Integers
    hour_ = StringVar()
    hour_.set(hours_array[0])
    minute_ = StringVar()
    minute_.set(hours_array[0])
    second_ = StringVar()
    second_.set(hours_array[0])

    # creating widget
    hour_dropdown = OptionMenu(
        add_window,
        hour_,
        *hours_array[:25]
    )

    minute_dropdown = OptionMenu(
        add_window,
        minute_,
        *hours_array
    )

    seconds_dropdown = OptionMenu(
        add_window,
        second_,
        *hours_array
    )

    confirm_add_button = Button(add_window, text = "Add")
    confirm_add_button.configure(command = lambda: add_alarm(hour_, minute_, second_))
    # positioning widget
    hour_dropdown.grid(row = 0, column = 0, padx=10, pady = 10)
    minute_dropdown.grid(row = 0, column = 1)
    seconds_dropdown.grid(row = 0, column = 2)
    confirm_add_button.grid(row = 0, column = 4)


current_time_label = Label(clock_window, font = ('calibri', 20, 'bold'),
            background = '#4180c4', foreground = 'white', text = "Current Time", justify = LEFT, width = 10
            ).grid(row = 0, column = 0, padx = 10, ipadx = 10)

current_time = Label(clock_window, borderwidth= 40, font = ('calibri', 20, 'bold'),
            foreground = 'darkred', relief = "sunken", background = "darkgrey", justify = LEFT)

next_alarm_label = Label(clock_window, font = ('calibri', 20, 'bold'),
            background = '#4180c4', foreground = 'white', text = "Next Alarm", width = 10
            ).grid(row = 2, column = 0, padx = 10, ipadx = 10)

next_alarm = Label(clock_window, borderwidth = 2, font = ('calibri', 20, 'bold'),
            foreground = 'darkred', relief = "sunken", background = "darkgrey")

add_button = Button(clock_window, text = "Add")
add_button.configure(command = lambda: add_alarm_display())
alarms_button = Button(clock_window, text = "List Alarms")
alarms_button.configure(command=lambda: list_alarms())
snooze_button = Button(clock_window, text = "Snooze")
snooze_button.configure(command = lambda: snooze_alarm())
off_button = Button(clock_window, text = "Off")
off_button.configure(command=lambda: stop_alarm())


current_time.grid(row = 1, column = 0, padx = 10, pady = 10, 
            ipadx = 10)
next_alarm.grid(row = 3, column = 0, padx = 10, pady = 10, 
            ipadx = 10)

add_button.place(x = 250, y = 20)
alarms_button.place(x = 250, y = 40)
snooze_button.place(x = 250, y = 60)
off_button.place(x = 250, y = 80)

def time():
    string = strftime('%H:%M:%S')
    front = alarms.queue[0][1]
    current_time.config(text = string)
    current_time.after(1000, time)
    next_alarm.config(text = front)
    next_alarm.after(1000, time) 

time()
mainloop()
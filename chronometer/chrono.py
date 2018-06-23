#!/usr/bin/env python3
from tkinter import Tk, Label, Button
from time import time
from os import path

class Chrono:

    seconds_file = path.join(path.dirname(path.realpath(__file__)), "./seconds.txt")

    def __init__(self, master):

        self.time_format = "{hours:02}:{minutes:02}:{seconds:02}"

        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

        self.master = master
        master.title("Chronometer")

        self.time_label = Label(master, text=self.time_format.format(**self.convert_time_format(self.previous_time)))
        self.time_label.config(font=("Sans", 40))
        self.time_label.pack()

        self.start_stop_button = Button(master, text="Start/Stop", command=self.start_stop)
        self.start_stop_button.config(font=("Sans", 15))
        self.start_stop_button.pack()

        self.restart_button = Button(master, text="Reset", command=self.reset)
        self.restart_button.config(font=("Sans", 10))
        self.restart_button.pack()

    @property
    def previous_time(self):
        try:
            with open(self.seconds_file) as f:
                return float(f.read())
        except:
            return 0

    @previous_time.setter
    def previous_time(self, value):
        with open(self.seconds_file, 'w') as f:
            f.write(str(value))

    def start_stop(self):
        if self.running:
            print("Stop chrono!")
            self.previous_time = self.elapsed_time
            self.running = False
        else:
            print("Start chrono!")
            self.start_time = time()
            self.running = True
            self.refresh()

    def reset(self):
        print("Reset chrono!")
        self.elapsed_time = 0
        self.previous_time = 0
        self.running = False
        self.time_label.configure(text=self.time_format.format(**self.convert_time_format(0)))

    def refresh(self):
        if self.running:
            self.elapsed_time = time() - self.start_time + self.previous_time
            self.time_label.configure(text=self.time_format.format(**self.convert_time_format(self.elapsed_time)))
            self.master.after(1000, self.refresh) # every second...

    def convert_time_format(self, total_seconds):
        hours = int(total_seconds) / 3600
        remainder = int(total_seconds) % 3600
        minutes = remainder / 60
        seconds = remainder % 60
        return {"hours": int(hours), "minutes": int(minutes), "seconds": int(seconds)}


root = Tk()
chrono = Chrono(root)
root.mainloop()

from tkinter import *
#import time library to obtain current time
import time

#create a function timing and variable current_time
def timing():
    #display current hour,minute,seconds
    current_time = time.strftime("%H : %M : %S")
    #configure the clock
    clock.config(text=current_time)
    #clock will change after every 200 microseconds
    clock.after(200,timing)

#Create a variable that will store our tkinter window
root=Tk()
#set window background
root.configure(bg='black')

root.resizable(False, False)
#define size of the window
root.geometry("250x50")
#create a variable clock and store label
#First label will show time, second label will show hour:minute:second, third label will show the top digital clock
clock=Label(root, fg = 'cyan', bg='black', font=("times",30,"bold"))
clock.pack(anchor='center')
#clock.grid(row=3,column=2)
timing()

 
root.mainloop()
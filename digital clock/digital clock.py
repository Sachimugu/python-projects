from tkinter import *
#import time library to obtain current time
import time
from datetime import date

#create a function timing and variable current_time
def timing():
    #display current hour,minute,seconds
    current_time = time.strftime("%H : %M : %S")
    #configure the clock
    clock.config(text=current_time)
    #clock will change after every 200 microseconds
    clock.after(200,timing)

def datet():
    #display current hour,minute,seconds
    current_date = date.today()
    #configure the clock
    #datet.config(text=current_date)
    #clock will change after every 200 microseconds
    #datet.after(200,timing)
    

#Create a variable that will store our tkinter window
root=Tk()
#set window background
root.configure(bg='black')

root.resizable(False, False)
#define size of the window
root.geometry("200x56")
#create a variable clock and store label
#First label will show time, second label will show hour:minute:second, third label will show the top digital clock
clock=Label(root, fg = 'cyan', bg='black', font=("times",30,"bold"))
clock.place(x=5, y=0)#pack(side= BOTTOM,anchor='center')
current_date=Label(root, text=date.today(), fg = '#032929', bg='black', font=("Helvetica",10,"bold"))
current_date.place(x=60, y=40)
#clock.grid(row=3,column=2)
timing()
datet()

 
root.mainloop()
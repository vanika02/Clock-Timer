import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import pygame


# Tk() to create the main window in tkinter, we use the Tk class
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", root.destroy) # ensure process ends 
root.minsize(600, 600)

# initializing pygame and pygame mixer
pygame.init()



root.title("TIMER CLOCK")

# Creating a label 
tk.Label(root, text="TIMER CLOCK").pack()


# creating a clock using canvas

def digital_Clock():
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))
    cm_time = ist_time.strftime("%Y-%m-%D %H:%M:%S")
    day, timez = cm_time.split(' ')
    lbl.config(text=timez)
    lbl.after(1000, digital_Clock)

lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center', fill='x')
digital_Clock()


def timer_completed():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()
    messagebox.showerror("Done", "Time is completed")
    time.sleep(6) # time sleep for 3 seconds
    pygame.mixer.music.stop()
    pygame.quit()

# creating start and end buttons 
input_Value = tk.Entry(root)
input_Value.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')

print(time.time())
def get_input_value():
    Value = input_Value.get()
    try:
        num = int(Value)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

    num_sec = (num * 1000)

    root.after(num_sec, timer_completed)


input_Value_button = tk.Button(root, text="ENTER TIME IN SECONDS", command=get_input_value, width=20, height=2).pack(padx=5, pady=5, ipadx=10, ipady=10, fill='x') 









root.mainloop()
# mainloop() methos is used to run application once it's ready
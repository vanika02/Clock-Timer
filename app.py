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

timer_running = False
timer_id = None

def timer_completed():
    global timer_running
    timer_running = False
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()
    enable_buttons()
    messagebox.showinfo("Done", "Time is completed")
    time.sleep(6) # time sleep for 3 seconds
    pygame.mixer.music.stop()
    pygame.quit()

# creating start and end buttons 
input_Value = tk.Entry(root)
input_Value.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')



def get_input_value(unit):
    global timer_id, timer_running
    if timer_running:
        messagebox.showerror("Timer running", "Please wait until the time is finished or stop it to start a new one")
        return
    # disable buttons when the timer starts
    disable_buttons()

    Value = input_Value.get()
    try:
        num = int(Value)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

    if unit == "seconds":
        num_sec = (num * 1000)
    elif unit == "minutes":
        num_sec = (num * 60 * 1000)
    elif unit == "hours":
        num_sec = (num * 60 * 60 * 1000 )

    timer_running = True
    timer_id = root.after(num_sec, timer_completed)

def stop_timer():
    global timer_running, timer_id
    if timer_running and timer_id:
        root.after_cancel(timer_id)
        timer_running=False
        enable_buttons() # re enable all the buttons
        messagebox.showinfo("stopped", "Timer stopped before completion")

def disable_buttons():
    button_1.config(state="disabled")
    button_2.config(state="disabled")
    button_3.config(state="disabled")

def enable_buttons():
    button_1.config(state="normal")
    button_2.config(state="normal")
    button_3.config(state="normal")

frame = tk.Frame(root)
frame.pack()
button_1 = tk.Button(frame, text="SECONDS", command=lambda:get_input_value("seconds"), width=18, height=2, bg="green", fg="White")
button_1.grid(row=1, column = 0, padx=5, pady=2)
button_2 = tk.Button(frame, text="MINUTES", command=lambda:get_input_value("minutes"), width=18, height=2, bg="green", fg="White")
button_2.grid(row=1, column = 1, padx=5, pady=5) 
button_3 = tk.Button(frame, text="HOURS", command=lambda:get_input_value("hours"), width=18, height=2, bg="green", fg="White")
button_3.grid(row=1, column = 2, padx=5, pady=5)
stop_button = tk.Button(root, text="STOP", command=stop_timer, bg="red", fg="white", width=18, height=2)
stop_button.pack(pady=10, padx=10, fill='x')








root.mainloop()
# mainloop() methos is used to run application once it's ready
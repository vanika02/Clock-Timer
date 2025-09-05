import tkinter as tk
from tkinter import messagebox
import time

# Tk() to create the main window in tkinter, we use the Tk class

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", root.destroy) # ensure process ends 
root.minsize(600, 600)

root.title("TIMER CLOCK")

# Creating a label 
tk.Label(root, text="TIMER CLOCK").pack()

def start_clock():
    # get the time in seconds
    start = time.perf_counter()
    for i in range(10000):
        i = i+1
    end = time.perf_counter()
    print(end-start)

def timer_completed():
    messagebox.showerror("Done", "Time is completed")

# creating start and end buttons 
input_Value = tk.Entry(root)
input_Value.pack()

print(time.time())
def get_input_value():
    Value = input_Value.get()
    try:
        num = int(Value)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

    num_sec = (num * 1000)

    root.after(num_sec, timer_completed)


input_Value_button = tk.Button(root, text="ENTER TIME IN SECONDS", command=get_input_value).pack(padx=5, pady=5, fill='x') 
















root.mainloop()
# mainloop() methos is used to run application once it's ready
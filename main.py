'''
Name: Anthony Hardy
Date: Feb. 18, 2025
Purpose: Use pyOWM to display current weather conditions via tkinter.
Files: FIXME: ADD FILES USED
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.simpledialog import askstring
from tkinter import *
top = tk.Tk()
top.geometry("500x500")
'''
def askCity()
    cityName = askstring("Input","Enter in your city")
    print(cityName)

B = Button(top, text="Click", command=askCity)
B.place(x=50,y=50)
'''
frame = ttk.Frame(top)

label = ttk.Label(frame, text = "City")
label.pack(padx = 2)

separator = ttk.Separator(frame,orient= tk.HORIZONTAL)
separator.pack(expand = True, fill = tk.X)

label = ttk.Label(frame, text = "Current Temperature: x")
label.pack(padx = 5)

separator2 = ttk.Separator(frame,orient= tk.HORIZONTAL)
separator2.pack(expand=True,fill=tk.X)

label = ttk.Label(frame, text = "Current Alerts: Exam day!")
label.pack(padx = 5)



frame.pack(padx = 5, pady = 50, expand = True, fill = tk.BOTH)

top.mainloop()

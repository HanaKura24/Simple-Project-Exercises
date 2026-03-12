#Converter
import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.localization
ttkbootstrap.localization.initialize_localities = bool

#Window
window = ttk.Window(themename = "journal")
window.title("Demo")
window.geometry("600x300")

#Convert
def convert():
    mile = entry_int.get()
    km = mile * 1.61
    output_var.set(km)

#Title
title_label = ttk.Label(master = window, text = "Miles to kilometer", font = "Calibri 14 bold")
title_label.pack(pady= 20)

#Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry  = ttk.Entry(master = input_frame, textvariable = entry_int)
button  = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

#Output
output_var = tk.StringVar()
output = ttk.Label(master = window, text = "Output", font = "Calibri 10", textvariable = output_var)
output.pack(pady= 10)

#Run
window.mainloop()


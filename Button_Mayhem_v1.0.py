import tkinter as tk
from tkinter import ttk

# window
window =  tk.Tk()
window.title("Button Mayhem")
window.geometry("600x500")

# text var
prize = tk.StringVar()

# label
label = ttk.Label(window, text = "Choose a button and get a prize!", font = "Calibri 10 bold")
label.grid(row = 0, column = 0, columnspan = 3, pady = 15, padx = 25)

output = ttk.Label(window, textvariable = prize, font = "Calibri 10")
output.grid(row = 1, column = 0, columnspan = 3, pady = 15, padx = 25)

# button functions 
def lose(bt):
    prize.set("nope try again")
    bt["state"] = "disabled"
    
def win(bt):
    prize.set("You win!!! <3")
    # add reset all button 
    
    
# buttons
bt1 = ttk.Button(window, text = "button 1", command = lambda: lose(bt1))
bt1.grid(row = 2, column = 0, padx = 10, pady = 10)

bt2 = ttk.Button(window, text = "button 2",command = lambda: win(bt2))
bt2.grid(row = 2, column = 1, padx = 10, pady = 10)

bt3 = ttk.Button(window, text = "button 3", command = lambda: lose(bt3))
bt3.grid(row = 2, column = 2, padx = 10, pady = 10)

bt4 = ttk.Button(window, text = "button 4", command = lambda: lose(bt4))
bt4.grid(row = 3, column = 0, padx = 10, pady = 10)

bt5 = ttk.Button(window, text = "button 5",
command = lambda: lose(bt5))
bt5.grid(row = 3, column = 1, padx = 10, pady = 10)

bt6 = ttk.Button(window, text = "button 6", command = lambda: lose(bt6))
bt6.grid(row = 3, column = 2, padx = 10, pady = 10)

bt7 = ttk.Button(window , text = "button 7",
command = lambda: lose(bt7))
bt7.grid(row = 4, column = 0, padx = 10, pady = 10)

bt8 = ttk.Button(window , text = "button 8",
command = lambda: lose(bt8))
bt8.grid(row = 4, column = 1, padx = 10, pady = 10)

bt9 = ttk.Button(window , text = "button 9", command = lambda: win(bt9))
bt9.grid(row = 4, column = 2, padx = 10, pady = 10)

# running
window.mainloop()
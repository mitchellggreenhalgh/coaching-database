from tkinter import *
from tkinter import ttk

# Instantiate app
root = Tk()
root.title("Data Entry Tool")

# Widget functions
def test(*args):
    try:
        value = float(laps.get())
        distance_m.set(float(400 * value))
    
    except ValueError:  # ignore incorrect entries, no error
        pass

# Main GUI: Widget Configuration
mainframe = ttk.Frame(root, padding = "3 3 12 12")  # padding: left, top, right, bottom
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# Laps entry and display
laps = StringVar()
laps_entry = ttk.Entry(mainframe, width = 9, textvariable = laps)
laps_entry.grid(columns = 2, row = 1, sticky = (W, E))

distance_m = StringVar()
ttk.Label(mainframe, textvariable = distance_m).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text="Calculate Distance", command=test).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="laps").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="are equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():  # give padding between cells 
    child.grid_configure(padx=5 , pady=5)

laps_entry.focus()  # Focus on a particular widget
root.bind("<Return>", test)  # Optional bind a keystroke/shortcut instead of clicking the button

# Run app
# root.state('zoomed')  # start the window maximized
root.mainloop()
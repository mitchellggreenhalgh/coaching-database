from tkinter import *
from tkinter import ttk
from app_functions import frame_800
import sqlite3

# Instantiate app
root = Tk()
root.title('Data Entry Tool')

# Instantiate notebook
nb = ttk.Notebook(root)
nb.pack(fill='both', expand = 1)  # Puts the notebook widget into the root

# Widget format settings
frame_padding = '3 3 12 12'
frame_sticky = (N, S, E, W)
entry_sticky = (W, E)
label_sticky = entry_sticky
button_sticky = entry_sticky

# Database Connection
db_name = 'runningDB_master.db'

try: 
    with open('backup_database.py') as updater:
        exec(updater.read())
        print('DB update complete')
except:
    print('Recent backup within last 30 days found.')

# running_db = sqlite3.connect(db_name)
# connection = running_db.cursor()
# running_db.close()


# Race Splits Tab
race_splits_frame = ttk.Frame(nb, padding = frame_padding)
# race_splits.bind('<Control-Return>', entry fxn)
# race_splits.pack(fill='both', expand=1)

# Laps Tab
race_laps_frame = ttk.Frame(nb,padding = frame_padding)
# race_laps.bind('<Control-Return>', entry fxn)

#region <800m Tab>
db_800_frame = ttk.Frame(nb, padding = frame_padding)
db_800_frame.grid(column = 0, row = 0, sticky = frame_sticky)

def temp_fxn(*args):
    try:
        athlete_info = athlete_800.get()

        if first_200.get() != 0:
            entry_confirmation.set(f"Submitted {athlete_info}'s 200s to the Database")
            # athlete_800_entry.focus()  # Won't register in system because of scope i think

        elif first_400.get() != 0:
            entry_confirmation.set(f"Submitted {athlete_info}'s 400s to Database")
            
        else:
            entry_confirmation.set('All Zeros')
                
    except ValueError:
        pass

def enter_data_800():
    # db.connect
    # db.cursor
    # sql insert query
    # data.get() tuple that matches query
    # cursor.execute(query, data_tuple)
    # db.commit()
    # db.close_connection
    pass


ttk.Label(db_800_frame, text = 'Athlete (first last)').grid(column = 0, row = 0, sticky = label_sticky)
athlete_800 = StringVar()
athlete_800_entry = ttk.Entry(db_800_frame, width = 10, textvariable = athlete_800).grid(column = 0, row = 1, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '200 #1 (#.##)').grid(column = 1, row = 0, sticky = label_sticky)
first_200 = DoubleVar()
first_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_200).grid(column = 1, row = 1, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '200 #2 (#.##)').grid(column = 2, row = 0, sticky = label_sticky)
second_200 = DoubleVar()
second_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_200).grid(column = 2, row = 1, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '200 #3 (#.##)').grid(column = 3, row = 0, sticky = label_sticky)
third_200 = DoubleVar()
third_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = third_200).grid(column = 3, row = 1, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '200 #4 (#.##)').grid(column = 4, row = 0, sticky = label_sticky)
fourth_200 = DoubleVar()
fourth_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = fourth_200).grid(column = 4, row = 1, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '400 #1 (#.##)').grid(column = 1, row = 2, sticky = label_sticky)
first_400 = DoubleVar()
first_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_400).grid(column = 1, row = 3, sticky = entry_sticky)

ttk.Label(db_800_frame, text = '400 #2 (#.##)').grid(column = 2, row = 2, sticky = label_sticky)
second_400 = DoubleVar()
second_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_400).grid(column = 2, row = 3, sticky = entry_sticky)

entry_confirmation = StringVar()
ttk.Label(db_800_frame, textvariable = entry_confirmation).grid(column = 0, row = 6, sticky = label_sticky)
ttk.Button(db_800_frame, text = 'Submit', command = temp_fxn).grid(column = 3, row = 6, sticky = button_sticky)

for child in db_800_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.bind('<Control-Return>', temp_fxn)  # https://stackoverflow.com/questions/46345039/python-tkinter-binding-keypress-event-to-active-tab-in-ttk-notebook
#endregion


# 400m Tab
db_400_frame = ttk.Frame(nb, padding = frame_padding)
# db_400.bind('<Control-Return>', entry fxn)

nb.add(race_splits_frame, text = 'Race Splits')
nb.add(race_laps_frame, text = 'Race Lap Splits')
nb.add(db_800_frame, text = '800m Database')
nb.add(db_400_frame, text = '400m Database')

nb.select(db_800_frame)  # Select which tab to start on

root.mainloop()
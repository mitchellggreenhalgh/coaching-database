from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from widget_formats import universal_format as uf
from backup_database import db_backupper
import sqlite3

# Instantiate app
root = Tk()
root.title('Data Entry Tool')

# Instantiate notebook
nb = ttk.Notebook(root)
nb.pack(fill='both', expand = 1)  # Puts the notebook widget into the root

# Database Connection
db_name = db_backupper().db_name

# Backup Database
create_backup = db_backupper()
try: 
    create_backup._backup()

except:
    override_backup = messagebox.askyesno(title = 'Database Updater', message = 'Recent backup within last 30 days found. Backup database anyway?')
    if override_backup:
        create_backup._backup_override()
    else:
        messagebox.showinfo(title = 'Database Updater', message = 'No backup created')

#region <Athlete Tab>
athlete_frame = ttk.Frame(nb, padding = uf.frame_padding)
athlete_frame.grid(column = 0, row = 0, sticky = uf.frame_sticky)

def confirm_entries_athlete(*args):
    athlete_info = athlete_name.get().lower()    
    try:
        if athlete_school_year.get() != 0:
            entry_confirmation_athlete.set(f"Submitted {athlete_info}'s \ninformation to the database")
            enter_data_athlete()
        else:
            entry_confirmation_athlete.set(f"Please enter data")
            raise Exception
                
    except ValueError:
        pass

def enter_data_athlete():
    insert_query = '''
    INSERT INTO athletes (
        athlete, 
        school_year_beginning, 
        grade
    ) VALUES (?, ?, ?)
    '''

    insert_data = (athlete_name.get().lower(), 
                   athlete_school_year.get(), 
                   athlete_grade.get())
    
    running_db = sqlite3.connect(db_name)
    cursor = running_db.cursor()
    cursor.execute(insert_query, insert_data)
    running_db.commit()
    running_db.close()

ttk.Label(athlete_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = uf.label_sticky)
athlete_name = StringVar()
athlete_name_entry = ttk.Entry(athlete_frame, width = 10, textvariable = athlete_name).grid(column = 0, row = 1, sticky = uf.entry_sticky)

ttk.Label(athlete_frame, text = 'School Year (fall semester year) [yyyy]').grid(column = 1, row = 0, sticky = uf.label_sticky)
athlete_school_year = IntVar()
athlete_school_year_entry = ttk.Entry(athlete_frame, width = 10, textvariable = athlete_school_year).grid(column = 1, row = 1, sticky = uf.entry_sticky)

ttk.Label(athlete_frame, text = 'Grade [#, 9-12]').grid(column = 2, row = 0, sticky = uf.label_sticky)
athlete_grade = IntVar()
athlete_grade_entry = ttk.Entry(athlete_frame, width = 10, textvariable = athlete_grade).grid(column = 2, row = 1, sticky = uf.entry_sticky)

entry_confirmation_athlete = StringVar()    
ttk.Label(athlete_frame, textvariable = entry_confirmation_athlete).grid(column = 0, row = 2, sticky = uf.label_sticky)
ttk.Button(athlete_frame, text = 'Submit', command = confirm_entries_athlete).grid(column = 3, row = 1, sticky = uf.button_sticky)

for child in athlete_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
#endregion

#region <Race Splits Tab>
splits_frame = ttk.Frame(nb, padding = uf.frame_padding)
splits_frame.grid(column = 0, row = 0, sticky = uf.frame_sticky)

def confirm_entries_splits(*args):
    raise NotImplementedError

def enter_data_splits(_distance):
    # race_distance_m.get(): make dictionary of key:distance, value:entry fxn specific for that distance (do the math before entering it into a database?)
    raise NotImplementedError

ttk.Label(splits_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = uf.label_sticky)
splits_athlete = StringVar()
splits_athlete_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_athlete).grid(column = 0, row = 1, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Event Distance [#### meters]').grid(column = 1, row = 0, sticky = uf.label_sticky)
splits_event = IntVar()
splits_event_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_event).grid(column = 1, row = 1, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Date [yyyy-mm-dd]').grid(column = 2, row = 0, sticky = uf.label_sticky)
splits_date = StringVar()
splits_date_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_date).grid(column = 2, row = 1, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Meet Name [aaa bbb]').grid(column = 3, row = 0, sticky = uf.label_sticky)
splits_meet = StringVar()
splits_meet_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_meet).grid(column = 3, row = 1, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Relay Split? (y/n) [1/0]').grid(column = 4, row = 0, sticky = uf.label_sticky)
splits_relay = IntVar()
splits_relay_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_relay).grid(column = 4, row = 1, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Split 1 [mm:ss.dd]').grid(column = 0, row = 2, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 2 [mm:ss.dd]').grid(column = 1, row = 2, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 3 [mm:ss.dd]').grid(column = 2, row = 2, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 4 [mm:ss.dd]').grid(column = 3, row = 2, sticky = uf.label_sticky)
splits_split_1 = StringVar()
splits_split_2 = StringVar()
splits_split_3 = StringVar()
splits_split_4 = StringVar()
splits_split_1_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_1).grid(column = 0, row = 3, sticky = uf.entry_sticky)
splits_split_2_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_2).grid(column = 1, row = 3, sticky = uf.entry_sticky)
splits_split_3_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_3).grid(column = 2, row = 3, sticky = uf.entry_sticky)
splits_split_4_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_4).grid(column = 3, row = 3, sticky = uf.entry_sticky)

ttk.Label(splits_frame, text = 'Split 5 [mm:ss.dd]').grid(column = 0, row = 4, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 6 [mm:ss.dd]').grid(column = 1, row = 4, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 7 [mm:ss.dd]').grid(column = 2, row = 4, sticky = uf.label_sticky)
ttk.Label(splits_frame, text = 'Split 8 [mm:ss.dd]').grid(column = 3, row = 4, sticky = uf.label_sticky)
splits_split_5 = StringVar()
splits_split_6 = StringVar()
splits_split_7 = StringVar()
splits_split_8 = StringVar()
splits_split_5_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_5).grid(column = 0, row = 5, sticky = uf.entry_sticky)
splits_split_6_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_6).grid(column = 1, row = 5, sticky = uf.entry_sticky)
splits_split_7_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_7).grid(column = 2, row = 5, sticky = uf.entry_sticky)
splits_split_8_entry = ttk.Entry(splits_frame, width = 10, textvariable = splits_split_8).grid(column = 3, row = 5, sticky = uf.entry_sticky)

entry_confirmation_splits = StringVar()    
ttk.Label(splits_frame, textvariable = entry_confirmation_splits).grid(column = 4, row = 4, sticky = uf.label_sticky)
ttk.Button(splits_frame, text = 'Submit', command = confirm_entries_splits).grid(column = 4, row = 5, sticky = uf.button_sticky)

for child in splits_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
#endregion

#region <Laps Tab>
laps_frame = ttk.Frame(nb, padding = uf.frame_padding)
laps_frame.grid(column = 0, row = 0, sticky = uf.frame_sticky)

def confirm_entries_laps(*args):
    raise NotImplementedError

def enter_data_laps(_distance):
    # race_distance_m.get(): make dictionary of key:distance, value:entry fxn specific for that distance (do the math before entering it into a database?)
    raise NotImplementedError

ttk.Label(laps_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = uf.label_sticky)
laps_athlete = StringVar()
laps_athlete_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_athlete).grid(column = 0, row = 1, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Event Distance [#### meters]').grid(column = 1, row = 0, sticky = uf.label_sticky)
laps_event = IntVar()
laps_event_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_event).grid(column = 1, row = 1, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Date [yyyy-mm-dd]').grid(column = 2, row = 0, sticky = uf.label_sticky)
laps_date = StringVar()
laps_date_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_date).grid(column = 2, row = 1, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Meet Name [aaa bbb]').grid(column = 3, row = 0, sticky = uf.label_sticky)
laps_meet = StringVar()
laps_meet_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_meet).grid(column = 3, row = 1, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Relay Split? (y/n) [1/0]').grid(column = 4, row = 0, sticky = uf.label_sticky)
laps_relay = IntVar()
laps_relay_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_relay).grid(column = 4, row = 1, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Lap 1 [mm:ss.dd]').grid(column = 0, row = 2, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 2 [mm:ss.dd]').grid(column = 1, row = 2, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 3 [mm:ss.dd]').grid(column = 2, row = 2, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 4 [mm:ss.dd]').grid(column = 3, row = 2, sticky = uf.label_sticky)
laps_lap_1 = StringVar()
laps_lap_2 = StringVar()
laps_lap_3 = StringVar()
laps_lap_4 = StringVar()
laps_lap_1_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_1).grid(column = 0, row = 3, sticky = uf.entry_sticky)
laps_lap_2_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_2).grid(column = 1, row = 3, sticky = uf.entry_sticky)
laps_lap_3_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_3).grid(column = 2, row = 3, sticky = uf.entry_sticky)
laps_lap_4_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_4).grid(column = 3, row = 3, sticky = uf.entry_sticky)

ttk.Label(laps_frame, text = 'Lap 5 [mm:ss.dd]').grid(column = 0, row = 4, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 6 [mm:ss.dd]').grid(column = 1, row = 4, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 7 [mm:ss.dd]').grid(column = 2, row = 4, sticky = uf.label_sticky)
ttk.Label(laps_frame, text = 'Lap 8 [mm:ss.dd]').grid(column = 3, row = 4, sticky = uf.label_sticky)
laps_lap_5 = StringVar()
laps_lap_6 = StringVar()
laps_lap_7 = StringVar()
laps_lap_8 = StringVar()
laps_lap_5_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_5).grid(column = 0, row = 5, sticky = uf.entry_sticky)
laps_lap_6_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_6).grid(column = 1, row = 5, sticky = uf.entry_sticky)
laps_lap_7_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_7).grid(column = 2, row = 5, sticky = uf.entry_sticky)
laps_lap_8_entry = ttk.Entry(laps_frame, width = 10, textvariable = laps_lap_8).grid(column = 3, row = 5, sticky = uf.entry_sticky)

entry_confirmation_laps = StringVar()    
ttk.Label(laps_frame, textvariable = entry_confirmation_laps).grid(column = 4, row = 4, sticky = uf.label_sticky)
ttk.Button(laps_frame, text = 'Submit', command = confirm_entries_laps).grid(column = 4, row = 5, sticky = uf.button_sticky)

for child in laps_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
#endregion

#region <800m Tab> 
db_800_frame = ttk.Frame(nb, padding = uf.frame_padding)
db_800_frame.grid(column = 0, row = 0, sticky = uf.frame_sticky)

def confirm_entries_800(*args):
    athlete_info = athlete_800.get().lower()    
    try:
        
        if first_200.get() != 0 and first_400.get() == 0:
            entry_confirmation_800.set(f"Submitted {athlete_info}'s 200s to the database")
            enter_data_800()

        elif first_400.get() != 0 and first_200.get() == 0:
            entry_confirmation_800.set(f"Submitted {athlete_info}'s 400s to database")
            enter_data_800()

        elif first_200.get() != 0 and first_400.get() != 0:
            entry_confirmation_800.set(f"Submitted {athlete_info}'s results to database")
            enter_data_800()

        else:
            entry_confirmation_800.set('All Zeros')
            raise Exception('No data entered')
                
    except ValueError:
        pass

def enter_data_800():
    insert_query = '''
    INSERT INTO db800 (
        athlete, 
        first_200, second_200, third_200, fourth_200,
        first_400, second_400
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    '''

    insert_data = (athlete_800.get().lower(), 
                   first_200.get(), second_200.get(), third_200.get(), fourth_200.get(),
                   first_400.get(), second_400.get())
    
    running_db = sqlite3.connect(db_name)
    cursor = running_db.cursor()
    cursor.execute(insert_query, insert_data)
    running_db.commit()
    running_db.close()
    

ttk.Label(db_800_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = uf.label_sticky)
athlete_800 = StringVar()
athlete_800_entry = ttk.Entry(db_800_frame, width = 10, textvariable = athlete_800).grid(column = 0, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '200 #1 [#.##]').grid(column = 1, row = 0, sticky = uf.label_sticky)
first_200 = DoubleVar()
first_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_200).grid(column = 1, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '200 #2 [#.##]').grid(column = 2, row = 0, sticky = uf.label_sticky)
second_200 = DoubleVar()
second_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_200).grid(column = 2, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '200 #3 [#.##]').grid(column = 3, row = 0, sticky = uf.label_sticky)
third_200 = DoubleVar()
third_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = third_200).grid(column = 3, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '200 #4 [#.##]').grid(column = 4, row = 0, sticky = uf.label_sticky)
fourth_200 = DoubleVar()
fourth_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = fourth_200).grid(column = 4, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '400 #1 [#.##]').grid(column = 1, row = 2, sticky = uf.label_sticky)
first_400 = DoubleVar()
first_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_400).grid(column = 1, row = 3, sticky = uf.entry_sticky)

ttk.Label(db_800_frame, text = '400 #2 [#.##]').grid(column = 2, row = 2, sticky = uf.label_sticky)
second_400 = DoubleVar()
second_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_400).grid(column = 2, row = 3, sticky = uf.entry_sticky)

entry_confirmation_800 = StringVar()
ttk.Label(db_800_frame, textvariable = entry_confirmation_800).grid(column = 0, row = 6, sticky = uf.label_sticky)
ttk.Button(db_800_frame, text = 'Submit', command = confirm_entries_800).grid(column = 3, row = 6, sticky = uf.button_sticky)

for child in db_800_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.bind('<Control-Return>', confirm_entries_800)  # https://stackoverflow.com/questions/46345039/python-tkinter-binding-keypress-event-to-active-tab-in-ttk-notebook

#endregion

#region <400m Tab>  #TODO: rename first_200 and second_200
db_400_frame = ttk.Frame(nb, padding = uf.frame_padding)
db_400_frame.grid(column = 0, row = 0, sticky = uf.frame_sticky)

def confirm_entries_400(*args):
    athlete_info = athlete_400.get().lower()    
    try:
        if first_200.get() != 0:
            entry_confirmation_400.set(f"Submitted {athlete_info}'s 200s to the database")
            enter_data_400()
            
        else:
            entry_confirmation_400.set('All Zeros')
            raise Exception('No data entered')
                
    except ValueError:
        pass

def enter_data_400():
    insert_query = '''
    INSERT INTO db400 (
        athlete, 
        first_200, second_200
    ) VALUES (?, ?, ?)
    '''

    insert_data = (athlete_400.get().lower(), 
                   first_200.get(), second_200.get())
    
    running_db = sqlite3.connect(db_name)
    cursor = running_db.cursor()
    cursor.execute(insert_query, insert_data)
    running_db.commit()
    running_db.close()
    

ttk.Label(db_400_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = uf.label_sticky)
athlete_400 = StringVar()
athlete_400_entry = ttk.Entry(db_400_frame, width = 10, textvariable = athlete_400).grid(column = 0, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_400_frame, text = '200 #1 [#.##]').grid(column = 1, row = 0, sticky = uf.label_sticky)
first_200 = DoubleVar()
first_200_entry = ttk.Entry(db_400_frame, width = 10, textvariable = first_200).grid(column = 1, row = 1, sticky = uf.entry_sticky)

ttk.Label(db_400_frame, text = '200 #2 [#.##]').grid(column = 2, row = 0, sticky = uf.label_sticky)
second_200 = DoubleVar()
second_200_entry = ttk.Entry(db_400_frame, width = 10, textvariable = second_200).grid(column = 2, row = 1, sticky = uf.entry_sticky)

entry_confirmation_400 = StringVar()
ttk.Label(db_400_frame, textvariable = entry_confirmation_400).grid(column = 0, row = 2, sticky = uf.label_sticky)
ttk.Button(db_400_frame, text = 'Submit', command = confirm_entries_400).grid(column = 3, row = 1, sticky = uf.button_sticky)

for child in db_400_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

#endregion

#TODO: Meet info entry

nb.add(athlete_frame, text = 'Athlete Info')
nb.add(splits_frame, text = 'Race Splits')
nb.add(laps_frame, text = 'Lap Splits')
nb.add(db_800_frame, text = '800m Database')
nb.add(db_400_frame, text = '400m Database')

nb.select(splits_frame)  # Select which tab to start on

root.mainloop()
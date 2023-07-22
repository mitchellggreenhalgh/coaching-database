#region <800m Tab>
db_800_frame = ttk.Frame(nb, padding = formats.frame_padding)
db_800_frame.grid(column = 0, row = 0, sticky = formats.frame_sticky)

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
    
    db_ops.submit_data(db_name, insert_query, insert_data)
    

ttk.Label(db_800_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = formats.label_sticky)
athlete_800 = StringVar()
athlete_800_entry = ttk.Entry(db_800_frame, width = 10, textvariable = athlete_800).grid(column = 0, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '200 #1 [#.##]').grid(column = 1, row = 0, sticky = formats.label_sticky)
first_200 = DoubleVar()
first_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_200).grid(column = 1, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '200 #2 [#.##]').grid(column = 2, row = 0, sticky = formats.label_sticky)
second_200 = DoubleVar()
second_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_200).grid(column = 2, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '200 #3 [#.##]').grid(column = 3, row = 0, sticky = formats.label_sticky)
third_200 = DoubleVar()
third_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = third_200).grid(column = 3, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '200 #4 [#.##]').grid(column = 4, row = 0, sticky = formats.label_sticky)
fourth_200 = DoubleVar()
fourth_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = fourth_200).grid(column = 4, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '400 #1 [#.##]').grid(column = 1, row = 2, sticky = formats.label_sticky)
first_400 = DoubleVar()
first_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_400).grid(column = 1, row = 3, sticky = formats.entry_sticky)

ttk.Label(db_800_frame, text = '400 #2 [#.##]').grid(column = 2, row = 2, sticky = formats.label_sticky)
second_400 = DoubleVar()
second_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_400).grid(column = 2, row = 3, sticky = formats.entry_sticky)

entry_confirmation_800 = StringVar()
ttk.Label(db_800_frame, textvariable = entry_confirmation_800).grid(column = 0, row = 6, sticky = formats.label_sticky)
ttk.Button(db_800_frame, text = 'Submit', command = confirm_entries_800).grid(column = 3, row = 6, sticky = formats.button_sticky)

for child in db_800_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.bind('<Control-Return>', confirm_entries_800)  # https://stackoverflow.com/questions/46345039/python-tkinter-binding-keypress-event-to-active-tab-in-ttk-notebook

#endregion

#region <400m Tab>
db_400_frame = ttk.Frame(nb, padding = formats.frame_padding)
db_400_frame.grid(column = 0, row = 0, sticky = formats.frame_sticky)

def confirm_entries_400(*args):
    athlete_info = athlete_400.get().lower()    
    try:
        if first_200_400.get() != 0:
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
                   first_200_400.get(), second_200_400.get())
    
    db_ops.submit_data(db_name, insert_query, insert_data)
    

ttk.Label(db_400_frame, text = 'Athlete [first last]').grid(column = 0, row = 0, sticky = formats.label_sticky)
athlete_400 = StringVar()
athlete_400_entry = ttk.Entry(db_400_frame, width = 10, textvariable = athlete_400).grid(column = 0, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_400_frame, text = '200 #1 [#.##]').grid(column = 1, row = 0, sticky = formats.label_sticky)
first_200_400 = DoubleVar()
first_200_400_entry = ttk.Entry(db_400_frame, width = 10, textvariable = first_200_400).grid(column = 1, row = 1, sticky = formats.entry_sticky)

ttk.Label(db_400_frame, text = '200 #2 [#.##]').grid(column = 2, row = 0, sticky = formats.label_sticky)
second_200_400 = DoubleVar()
second_200_400_entry = ttk.Entry(db_400_frame, width = 10, textvariable = second_200_400).grid(column = 2, row = 1, sticky = formats.entry_sticky)

entry_confirmation_400 = StringVar()
ttk.Label(db_400_frame, textvariable = entry_confirmation_400).grid(column = 0, row = 2, sticky = formats.label_sticky)
ttk.Button(db_400_frame, text = 'Submit', command = confirm_entries_400).grid(column = 3, row = 1, sticky = formats.button_sticky)

for child in db_400_frame.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
#endregion

nb.add(db_800_frame, text = '800m Database', state = 'hidden')  # TODO: Move these to their own app
nb.add(db_400_frame, text = '400m Database', state = 'hidden')
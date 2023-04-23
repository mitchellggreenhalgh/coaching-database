from tkinter import *
from tkinter import ttk
from widget_formats import universal_format as formats
import sqlite3
from backup_database import db_backupper as dbb


class frame_800:
    def __init__(self, notebook:ttk.Notebook):
        self.notebook = notebook

    def confirm_entries(self, *args):
        ''' Submit data and return confirmation to app '''

        athlete_info = self.athlete_800.get().lower()    
        try:
            if self.first_200.get() != 0 and self.first_400.get() == 0:
                self.entry_confirmation.set(f"Submitted {athlete_info}'s 200s to the database")
                # athlete_800_entry.focus()  # Won't register in system because of scope i think

            elif self.first_400.get() != 0 and self.first_200.get() == 0:
                self.entry_confirmation.set(f"Submitted {athlete_info}'s 400s to database")
            
            elif self.first_200.get() != 0 and self.first_400.get() != 0:
                self.entry_confirmation.set(f"Submitted {athlete_info}'s results to database")
                
            else:
                self.entry_confirmation.set('All Zeros')
                    
            self.enter_data_800()

        except ValueError:
            pass

    def enter_data_800(self):
        ''' Use SQLite queries to enter 800m results into database '''

        insert_query = '''
        INSERT INTO db800 (
            athlete, 
            first_200, second_200, third_200, fourth_200,
            first_400, second_400
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        '''

        insert_data = (self.athlete_800.get().lower(), 
                    self.first_200.get(), self.second_200.get(), self.third_200.get(), self.fourth_200.get(),
                    self.first_400.get(), self.second_400.get())
        
        running_db = sqlite3.connect(dbb.db_name)
        cursor = running_db.cursor()
        cursor.execute(insert_query, insert_data)
        running_db.commit()
        running_db.close()
    
    
    db_800_frame = ttk.Frame(self.notebook, padding = formats.frame_padding)
    db_800_frame.grid(column = 0, row = 0, sticky = formats.frame_sticky)

    ttk.Label(db_800_frame, text = 'Athlete (first last)').grid(column = 0, row = 0, sticky = formats.label_sticky)
    athlete_800 = StringVar()
    athlete_800_entry = ttk.Entry(db_800_frame, width = 10, textvariable = athlete_800).grid(column = 0, row = 1, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '200 #1 (#.##)').grid(column = 1, row = 0, sticky = formats.label_sticky)
    first_200 = DoubleVar()
    first_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_200).grid(column = 1, row = 1, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '200 #2 (#.##)').grid(column = 2, row = 0, sticky = formats.label_sticky)
    second_200 = DoubleVar()
    second_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_200).grid(column = 2, row = 1, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '200 #3 (#.##)').grid(column = 3, row = 0, sticky = formats.label_sticky)
    third_200 = DoubleVar()
    third_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = third_200).grid(column = 3, row = 1, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '200 #4 (#.##)').grid(column = 4, row = 0, sticky = formats.label_sticky)
    fourth_200 = DoubleVar()
    fourth_200_entry = ttk.Entry(db_800_frame, width = 10, textvariable = fourth_200).grid(column = 4, row = 1, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '400 #1 (#.##)').grid(column = 1, row = 2, sticky = formats.label_sticky)
    first_400 = DoubleVar()
    first_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = first_400).grid(column = 1, row = 3, sticky = formats.entry_sticky)

    ttk.Label(db_800_frame, text = '400 #2 (#.##)').grid(column = 2, row = 2, sticky = formats.label_sticky)
    second_400 = DoubleVar()
    second_400_entry = ttk.Entry(db_800_frame, width = 10, textvariable = second_400).grid(column = 2, row = 3, sticky = formats.entry_sticky)

    entry_confirmation = StringVar()
    ttk.Label(db_800_frame, textvariable = entry_confirmation).grid(column = 0, row = 6, sticky = formats.label_sticky)
    ttk.Button(db_800_frame, text = 'Submit', command = confirm_entries).grid(column = 3, row = 6, sticky = formats.button_sticky)

    for child in db_800_frame.winfo_children():
        child.grid_configure(padx = 5, pady = 5)

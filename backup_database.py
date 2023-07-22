import os
from datetime import date, datetime, timedelta
from glob import glob
from shutil import copyfile
from tkinter import messagebox

class db_backupper:
    db_files =  glob('backup_DBs/backup*.db')
    now = datetime.now()
    timestamps = [datetime.fromtimestamp(os.path.getctime(db)) for db in db_files]
    backup_period = timedelta(days = 30)
    db_name = 'runningDB_master.db'
    db_backup_name = "backup_DBs/backup_runningDB_" + str(date.today()) + '.db'

    def _backup(self):
        time_since_backup = [self.now - tmstmp for tmstmp in self.timestamps]
        if not any(time < self.backup_period for time in time_since_backup):
                copyfile(self.db_name, self.db_backup_name)
                messagebox.showinfo(title = 'Database Updater', message = 'New backup created.')
        else:
            raise Exception('Recent backup within last 30 days found.')
    
    def _backup_override(self):
         copyfile(self.db_name, self.db_backup_name)
         messagebox.showinfo(title = 'Database Updater', message = 'New backup created.')

import os
from datetime import date, datetime, timedelta
from glob import glob
from shutil import copyfile

db_files = glob('backup_DBs/backup*.db')

time_since_backup = []
for db in db_files:
    time_since_backup.append(datetime.now() - datetime.fromtimestamp(os.path.getctime(db)))

backup_period = timedelta(days=30)
if not any(time < backup_period for time in time_since_backup):  # TODO override by removing 'not'
    try:
        db_name = 'runningDB_master.db'
        db_backup_name = "backup_DBs/backup_runningDB_" + str(date.today()) + '.db'
        copyfile(db_name, db_backup_name)
    
    except:
        pass
    
else:
    raise Exception('Recent backup within last 30 days found.')
    
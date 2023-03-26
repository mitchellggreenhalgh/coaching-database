import sqlite3  
from datetime import date, datetime, timedelta
import os
from glob import glob
# https://www.w3schools.com/sql/sql_view.asp


# Backup the database every 30 days. Check the date of all .db files, and if there's one within the last 30 days, cancel the new database. 
# #TODO: change it from making a brand new database to just making a copy of the last one
# #TODO: actually, just need to make an update_database.py, and only trigger this one if a .db can't be found
db_files = glob('*.db')

dbs_time_elapsed_since_backup = []
for db in db_files:
     dbs_time_elapsed_since_backup.append(datetime.now() - datetime.fromtimestamp(os.path.getctime(db)))

backup_period = timedelta(days=30)
if not any(time < backup_period for time in dbs_time_elapsed_since_backup):  # CURRENTLY SET TO KEEP REWRITING GIVEN RECENT DBs (remove 'not' to reset)
     print('Database recently backed up. No need to commit another version.')
     quit()


# Create Database
db_name = "runningDB_" + str(date.today()) + '.db'
running_db = sqlite3.connect(db_name)
connection = running_db.cursor()


# Setup DB structure
# TODO Other Tables: Records, Race splits/details, Meet information (weather, etc.), mileage and other individual based metrics (like intensity and stuff), data for other analyses (400/800 split ratio analyses)

connection.execute('''
                   CREATE TABLE IF NOT EXISTS athletes (
                    athlete TEXT,
                    school_year_beginning YEAR,
                    grade INTEGER,
                    PRIMARY KEY (athlete)
                   )
                   ''')

connection.execute('''
                   CREATE TABLE IF NOT EXISTS races (
                    athlete TEXT,
                    date DATE,
                    event_location TEXT,
                    event_name TEXT,
                    distance_m INTEGER,
                    time TIME,
                    PRIMARY KEY (athlete, date, distance_m)
                   )
                   ''')


# Commit Database
# This part is a bit redundant, need to merge with the #TODO on ln 9, but keeping it in for developing the database
try:
    # Check if a database of the same name exists
    if db_name not in os.listdir(path = os.getcwd()):
        running_db.commit()
    else: 
         raise Exception

except:
    overwrite_permission = input('Overwrite most recent database? [y]/n ')
    if overwrite_permission in ['', 'y']:
           running_db.commit()
           print('Database overwritten.')
    else:
           print('Commit canceled. Rename database.')

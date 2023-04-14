import sqlite3  
import os
# https://www.w3schools.com/sql/sql_view.asp


# Create Database
db_name = 'runningDB_master.db'
running_db = sqlite3.connect(db_name)
connection = running_db.cursor()


# Setup DB structure
# TODO Other Tables: Records (view of all races), race splits/details, Meet information (weather, etc.), mileage and other individual based metrics (like intensity and stuff)

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

connection.execute('''
                   CREATE TABLE IF NOT EXISTS db800 (
                    athlete TEXT,
                    first_200 DOUBLE,
                    second_200 DOUBLE,
                    third_200 DOUBLE,
                    fourth_200 DOUBLE,
                    first_400 DOUBLE,
                    second_400 DOUBLE,
                    time_200s AS (first_200 + second_200 + third_200 + fourth_200),
                    time_400s AS (first_400 + second_400),
                    PRIMARY KEY (athlete, first_200, second_200, third_200, fourth_200, first_400, second_400)
                    )
                   ''')

connection.execute('''
                   CREATE TABLE IF NOT EXISTS db400 (
                    athlete TEXT,
                    first_200 DOUBLE,
                    second_200 DOUBLE,
                    time_sec AS (first_200 + second_200),
                    PRIMARY KEY (athlete, first_200, second_200)
                    )
                   ''')


# Commit Database
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

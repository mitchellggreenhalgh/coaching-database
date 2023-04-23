import sqlite3  
import os
# https://www.w3schools.com/sql/sql_view.asp


# Create Database
db_name = 'runningDB_master.db'
running_db = sqlite3.connect(db_name)
connection = running_db.cursor()


# Setup DB structure
# TODO Other Tables: Records (view of all races), 
# race splits/details (table) --> TODO AXING THAT, gonna just convert the input from that into laps upon submitting data for insert,
# race laps/details (table) 
# relay table (overall time, participants, date)
# Meet information (weather, date, name, locationetc.), mileage and other individual based metrics (like intensity and stuff)

connection.execute('''
                   CREATE TABLE IF NOT EXISTS athletes (
                    athlete TEXT,
                    school_year_beginning YEAR,
                    grade INTEGER,
                    sex TEXT,
                    PRIMARY KEY (athlete)
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


connection.execute('''
                    CREATE TABLE IF NOT EXISTS race_laps (
                        athlete TEXT,
                        event_distance_m INTEGER,
                        date DATE,
                        meet_name TEXT,
                        relay_y_n INTEGER,
                        lap_1 TEXT,
                        lap_2 TEXT,
                        lap_3 TEXT,
                        lap_4 TEXT,
                        lap_5 TEXT,
                        lap_6 TEXT,
                        lap_7 TEXT,
                        lap_8 TEXT,
                        total_time TEXT,
                        PRIMARY KEY (athlete, event_distance_m, date, meet_name, total_time)
                    )
                   ''')

connection.execute('''
                    CREATE TABLE IF NOT EXISTS meet_information (
                        name TEXT,
                        date DATE,
                        host_school TEXT,
                        physical_location TEXT,
                        city_state TEXT,
                        weather_temperature_deg_F INTEGER,
                        weather_clouds TEXT,
                        weather_precipitation TEXT,
                        weather_notes TEXT
                   )
                   ''')

#TODO: RELAY TABLE

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

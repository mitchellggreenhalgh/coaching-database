import sqlite3  
import os
# https://www.w3schools.com/sql/sql_view.asp


class db_creator:
    def __init__(self, db_name = 'runningDB_master_2.db'):
        self.db_name = db_name

    def create_db(self):
        db_name = self.db_name
        running_db = sqlite3.connect(db_name)
        connection = running_db.cursor()

        connection.execute('''
                    CREATE TABLE IF NOT EXISTS athletes (
                        athlete TEXT,
                        season TEXT,
                        season_year YEAR,
                        grade INTEGER,
                        sex TEXT,
                        PRIMARY KEY (athlete, season, season_year)
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

    #TODO: add relative humidity to meet info? meh, dont really feel like looking up all the info retroactively
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
                            weather_notes TEXT,
                            PRIMARY KEY(name, date)
                    )
                    ''')

        connection.execute('''
                        CREATE TABLE IF NOT EXISTS relays (
                            meet_name TEXT,
                            date DATE,
                            event TEXT,
                            sex TEXT,
                            leg_1 TEXT,
                            leg_2 TEXT,
                            leg_3 TEXT,
                            leg_4 TEXT,
                            time TIME,
                            PRIMARY KEY (meet_name, date, event)
                        )
                        ''')
        
        connection.execute('''
                        CREATE TABLE IF NOT EXISTS seasons (
                           sport TEXT,
                           year YEAR,
                           start_date DATE,
                           end_date DATE
                        )
                           ''')

        try:
            # Check if a database of the same name exists
            if self.db_name not in os.listdir(path = os.getcwd()):
                running_db.commit()
                running_db.close()
            else: 
                raise Exception

        except:
            overwrite_permission = input('Overwrite most recent database? [y]/n ')
            if overwrite_permission in ['', 'y']:
                running_db.commit()
                print('Database overwritten.')
            else:
                print('Commit canceled. Rename database.')
    # Commit Database
        try:
            # Check if a database of the same name exists
            if self.db_name not in os.listdir(path = os.getcwd()):
                self.running_db.commit()
            else: 
                raise Exception

        except:
            overwrite_permission = input('Overwrite most recent database? [y]/n ')
            if overwrite_permission in ['', 'y']:
                running_db.commit()
                running_db.close()
                print('Database overwritten.')
            else:
                print('Commit canceled. Rename database.')

if __name__ == '__main__':
    new_db = db_creator()
    new_db.create_db()
    

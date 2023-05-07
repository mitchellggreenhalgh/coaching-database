import sqlite3

class db_ops:

    def submit_data(db_name, insert_query, insert_data):
        running_db = sqlite3.connect(db_name)
        cursor = running_db.cursor()
        cursor.execute(insert_query, insert_data)
        running_db.commit()
        running_db.close()
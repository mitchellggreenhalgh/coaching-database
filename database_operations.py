import sqlite3

class db_ops:

    def submit_data(db_name, insert_query, insert_data):
        running_db = sqlite3.connect(db_name)
        cursor = running_db.cursor()
        cursor.execute(insert_query, insert_data)
        running_db.commit()
        running_db.close()

    def retrieve_meets(db_name):
        running_db = sqlite3.connect(db_name)
        cursor = running_db.cursor()
        meets = cursor.execute('''
            SELECT DISTINCT name FROM meet_information
            ''')
        meet_list = [i[0] for i in meets]
        running_db.close()

        return meet_list
        
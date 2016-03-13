import sqlite3
import datetime
import csv
'''event_id=row[0], timestamp=row[2],
                    location_long=row[3], location_lat=row[4], individual_local_identifier = row[12],
                    study_name='white fronted goose'''
def import_csv(csv_file):
    f = open (csv_file, 'rt')
    try:
        reader = csv.reader(f)
        count = 0
        print ("test1")
        for row in reader:
            if (count != 1):
                row = row
                count = 1
                print ("test2")
            else:
                new_row = (row[0], row[2], row[3], row[4], row[12], 'white fronted goose')
                print (new_row)
                c.execute('''INSERT INTO raw_data (event_id, timestamp, location_long, location_lat,
                    individual_local_identifier, study_name) VALUES(?,?,?,?,?,?)''', new_row)       
    finally:
        f.close()


conn = sqlite3.connect('migrations.db')
c = conn.cursor()
c.execute('''CREATE TABLE raw_data
                (event_id, timestamp, location_long, location_lat,
                individual_local_identifier, study_name)''')

import_csv('data.csv')
conn.commit()
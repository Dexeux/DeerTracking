import sqlite3
import datetime
import csv
import time

def stringtoarr (input):
    year = input[0:4]
    month =input[5:7]
    day = input[8:10]
    hour = input[11:13]
    minute = input[14:16]
    second = input[17:19]
    dt = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
    unix = time.mktime(dt.timetuple())
    return unix
#print(stringtoarr("2006-03-23 20:52:00.000"))

'''event_id=row[0], timestamp=row[2],
                    location_long=row[3], location_lat=row[4], individual_local_identifier = row[12],
                    study_name='white fronted goose'''
def import_csv(csv_file):
    f = open (csv_file, 'rt')
    try:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if (count != 1):
                row = row
                count = 1
            else:
                new_row = (int(row[0]), int(stringtoarr(str(row[2]))), float(row[3]), float(row[4]), row[12], 'white fronted goose')
                print (new_row)
                c.execute('''INSERT INTO raw_data (event_id, timestamp, location_long, location_lat,
                    individual_local_identifier, study_name) VALUES(?,?,?,?,?,?)''', new_row)       
    finally:
        f.close()


conn = sqlite3.connect('migrations.db')
c = conn.cursor()
print (stringtoarr('2008-04-18 21:21:00.000'))
c.execute('''CREATE TABLE raw_data
                (event_id, timestamp, location_long, location_lat,
                individual_local_identifier, study_name)''')

import_csv('data.csv')
conn.commit()


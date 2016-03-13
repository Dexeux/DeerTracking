from numpy import *
from vectorseq import *
import sqlite3

conn = sqlite3.connect('migrations.db')
c = conn.cursor()

c.execute('SELECT individual_local_identifier FROM raw_data')
animal_id = c.fetchone()
c.execute('SELECT COUNT(individual_local_identifier) FROM raw_data')
num_points = c.fetchone()

c.execute('SELECT timestamp, location_long, location_lat FROM raw_data ORDER BY timestamp')
location_data = c.fetchall()

c.execute('SELECT timestamp FROM raw_data')
time_ref = c.fetchone()

for point in location_data:
    point(0) = point(0) - time_ref

# [(fdfdasfds, fdsafdsfasd, fdsafasdfa), (jfdsaljfasldkf,fsadjflkasdfj, fdasfdadsfa)]
x = zeros(num_points,2)
y = zeros(num_points,2)
z = zeros(num_points,2)
count = 0
for point in location_data:
    pos = tovector(point(1), point(2))
    x[count,0]= pos[0]
    x[count,1]= point(0)
    y[count,0]= pos[1]
    y[count,1]= point(0)
    z[count,0]= pos[2]
    z[count,1]= point(0)
    count += 1
    

    
    



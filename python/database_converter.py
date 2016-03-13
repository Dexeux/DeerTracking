from numpy import *
from vectorseq import *
from functions import *
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
xv = zeros(num_points-1,2)
yv = zeros(num_points-1,2)
zv = zeros(num_points-1,2)
vectorspeed = zeros(num_points-1,2)
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
    if count != len(location_data):
        next_point = location_data[count+1]
        posv = vectordiff(tovector(point(1),point(2)),tovector(next_point(1), next_point(2)))
        xv[count-1,0]= posv[0]
        xv[count-1,1]= point(0)
        yv[count-1,0]= posv[1]
        yv[count-1,1]= point(0)
        zv[count-1,0]= posv[2]
        zv[count-1,1]= point(0)
        vectorspeed[count-1,0] = vectorspeed(tovector(point(1),point(2)),point(0),tovector(next_point(1), next_point(2)),next_point(0))
        vectorspeed[count-1,1] = point(0)
aorder = 5
axval = linearapprox(matrix(x),aorder)
ayval = linearapprox(matrix(y),aorder)
azval = linearapprox(matrix(z),aorder)
vxval = linearapprox(matrix(xv),aorder)
yvval = linearapprox(matrix(yv),aorder)
zvval = linearapprox(matrix(zv),aorder)
speed = linearapprox(matrix(vectorspeed),aorder)

    



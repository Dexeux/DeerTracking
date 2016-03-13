from numpy import *
from vectorseq import *
from functions import *
import sqlite3
from equations import *
conn = sqlite3.connect('migrations.db')
c = conn.cursor()

c.execute('SELECT individual_local_identifier FROM raw_data')
animal_id = c.fetchone()
c.execute('SELECT COUNT(*) FROM raw_data')
num_points2 = c.fetchone()

num_points=int(num_points2[0])
print(type(num_points))

c.execute('SELECT timestamp, location_long, location_lat FROM raw_data ORDER BY timestamp')
location_data = c.fetchall()

c.execute('SELECT timestamp FROM raw_data')
time_tuple = c.fetchone()
time_ref = int(time_tuple[0])

time = []
for point_ref in location_data:
    value = point_ref[0] - time_ref
    time.append(value)

# [(fdfdasfds, fdsafdsfasd, fdsafasdfa), (jfdsaljfasldkf,fsadjflkasdfj, fdasfdadsfa)]

x = zeros((num_points,2))
y = zeros((num_points,2))
z = zeros((num_points,2))
xv = zeros((num_points-1,2))
yv = zeros((num_points-1,2))
zv = zeros((num_points-1,2))
vectorspeed1 = zeros((num_points-1,2))
count = 0
for point in location_data:
    pos = tovector(point[1], point[2])
    x[count,0]= pos[0]
    x[count,1]= time[count]
    y[count,0]= pos[1]
    y[count,1]= time[count]
    z[count,0]= pos[2]
    z[count,1]= time[count]
    count += 1
    if count != num_points:
        next_point = location_data[count]
        posv = vectordiff(tovector(point[1],point[2]),tovector(next_point[1], next_point[2]))
        xv[count-1,0]= posv[0]
        xv[count-1,1]= time[count]
        yv[count-1,0]= posv[1]
        yv[count-1,1]= time[count]
        zv[count-1,0]= posv[2]
        zv[count-1,1]= time[count]
        if time[count-1]!=time[count]:
            vectorspeed1[count-1,0] = vectorspeed(tovector(point[1],point[2]),int(time[count-1]),tovector(next_point[1], next_point[2]),int(time[count]))
            vectorspeed1[count-1,1] = time[count-1]
aorder = 15
axval = linearapprox(matrix(x),aorder)
ayval = linearapprox(matrix(y),aorder)
azval = linearapprox(matrix(z),aorder)
vxval = linearapprox(matrix(xv),aorder)
yvval = linearapprox(matrix(yv),aorder)
zvval = linearapprox(matrix(zv),aorder)
speed = linearapprox(matrix(vectorspeed1),aorder)

currentT = 0.05
newx = calculations(axval,currentT)
newy = calculations(ayval,currentT)
newz = calculations(azval,currentT)
speedT = calculations(speed,currentT)

newax = newx + speedT*calculations(vxval,currentT)
neway = newy + speedT*calculations(yvval,currentT)
newaz = newz + speedT*calculations(zvval,currentT)

pos1 = [newx,newy,newz]
pos2 = [newax,neway,newaz]
print(pos1)
print(pos2)
currentpos = tolong(pos1)
nextpos = tolong(pos2)

print(currentpos)
print(currentpos)
print(nextpos)
print(nextpos)

from numpy import *
#Make a vector from a long and lat
def tovector (longd,latd):
    longd =(math.pi)*(longd/180)
    latd =(math.pi)*(latd/180)
    r = 6371000*1.0
    z = r*sin(latd)
    n = r*cos(latd)
    x = n*cos(longd)
    y = n*sin(longd)
    pos = [x,y,z]
    return pos
def tolong(input):
    try:
        r = 6371000*1.0
        latd =math.asin(input[2]/r)
        n=sqrt(input[0]**2 + input[1]**2)
        longd = math.acos(n/r)
        longd = (longd/math.pi)*180
        latd = (latd/math.pi)*180
        pos = [longd,latd]
        return pos
    except ValueError:
        return int(0)
#input 2 arrays
def vectordiff(firstv,lastv):
    x = firstv[0] - lastv[0]
    y = firstv[1] - lastv[1]
    z = firstv[2] - lastv[2]
    scalar = sqrt(x**2 + y**2 + z**2)
    dist = [x/scalar,y/scalar,z/scalar]
    return dist
def vectoradd(posvec,movev):
    x = posvec[0] + movev[0]
    y = posvec[1] + movev[1]
    z = posvec[2] + movev[2]
    dist = [x,y,z]
    return dist
def vectorspeed(firstv,time1,lastv,time2):
    x = firstv[0] - lastv[0]
    y = firstv[1] - lastv[1]
    z = firstv[2] - lastv[2]
    deltat = (time2-time1)
    if deltat==0:
        deltat=1
    magdist = sqrt(x**2 + y**2 + z**2)
    speed = (magdist)/(deltat)
    return speed

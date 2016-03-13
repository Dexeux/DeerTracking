from numpy import *
def calculations (avalues,time):
    size = avalues.shape
    value = avalues[0]
    for vals in range (1, size[0]):
        value = value + avalues[vals]*time**(vals)
    return int(value)

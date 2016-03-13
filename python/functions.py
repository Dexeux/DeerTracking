from numpy import *

def linearapprox(inputvalues,order):
    #here we go boys
    #input is values [x,y] from matrix:    matrix([[x1,x2],[x2,y2],[x3,y3]])

    shape = inputvalues.shape
    ndata = shape[0]
    #find B
    bvalue = zeros((order+1,1))

    for b in range (0,order+1):
        datahold=0
        for n in range (0,ndata):
            datahold = datahold + inputvalues[n,1] * (inputvalues[n,0])**b
        bvalue[b,0]=datahold

    #create the matrix
    xvaluem = zeros((order+1,order+1))
    for b in range(0,order+1):
        for apos in range (0,order+1):
            datahold = 0
            for n in range(0,ndata):
                datahold = datahold + (inputvalues[n,0])**(b+apos)
            xvaluem[b,apos]=datahold
    
    #solve the matrix
    #print(type(xvaluem))
    #print(type(bvalue))
    inverse = linalg.inv(matrix(xvaluem))
    #print(type(inverse))
    avalues = inverse * matrix(bvalue)
    return(avalues)

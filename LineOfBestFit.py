import matplotlib.pyplot as plt
import numpy as np
N = 3
def sdev(coords):
    mean = sum(coords) / N

    sigmaN = 0
    #Sigma N is sigma new, and holds the ultimate value, while sigmaP holds the calculations
    for i in range(len(coords)):
        sigmaP = (coords[i] - mean)**2
        sigmaN += sigmaP
    #finally divide by N, used variance in case we need
    variance = sigmaN / (N - 1)
    standard_deviation = variance**.5
    return standard_deviation

def r(xcords, ycords):
    x_bar = sum(xcords) / 3
    y_bar = sum(ycords) / 3
    values = []
    for i in range(len(xcords)):
        #X part of the equation for r
        XV = (xcords[i] - x_bar)/sdev(xcords)
        #Y part
        YV = (ycords[i] - y_bar)/sdev(ycords)
        #finished the multiplied section and adding it to the values list, works since both lists are the same size
        values.append((XV*YV))
    #get the sum of all items/sigma part of equation, and then divide by n-1, which is 2 since the list has 3 items
    r = sum(values) / (N - 1)
    return r

def getB():
    cor = r(xcords, ycords)
    Sy = sdev(ycords)
    Sx = sdev(xcords)
    b = cor * (Sy/Sx)
    return b

def getA():
    y_bar = sum(ycords)/N
    x_bar = sum(xcords)/N
    b = getB()
    a = y_bar - (b*x_bar)
    return a



x1, y1 = [int(x) for x in input("Enter x1, y1\n").split(', ')]
x2, y2 = [int(x) for x in input("Enter x2, y2\n").split(', ')]
x3, y3 = [int(x) for x in input("Enter x3, y3\n").split(', ')]


xcords = [x1, x2, x3]
ycords = [y1, y2, y3]


Formula = "ŷ = {} + {}x".format(getA(), getB())
print(Formula)

x = np.linspace(min(xcords),max(xcords),100)
y = (getB()*x)+getA()
plt.plot(xcords, ycords, 'o')
plt.plot(x, y, '-r')
plt.show()




# seems a bit similar to the boat day

import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    #lst.sort()
    return lst

# every position, (including all the ones not listed) have coordinates (x,y,z)
# we can store all this in a list of ... 4x tuples ? ( is this basically another list ? )

# every point has (state, x ,y ,z)

# for every point, check adjacent and if conditions are met, swap.

def initDataStructure():
    # # = active or true, . = inactive or false
    points = []
    lst = getInput()
    z = 0 # this could be const probably
    x=0
    for ln in lst:
        y=0
        for char in ln:
            if char == "#":
                p = True
            else:
                p = False
            points.append([p,x,y,z])
            y+= 1
        x+= 1
    return points

def getAdjacency(point,points): # gets a single point, and checks the points around it
    return -1  # returns the number of adjacent active ( true) cubes

def changeData(p): # p is all the points and their states.
    return -1

def runGame(times):# how many times is the game run ?  (6)
    p = initDataStructure()
    x = 0
    while x < times:
        p = changeData(p)
    # count up the active cubes in P
    active = 0
    for z in p:
        if z[0] == True:
            active += 1
    return active

print(initDataStructure())

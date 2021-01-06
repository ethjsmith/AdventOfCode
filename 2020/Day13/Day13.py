import sys
from math import gcd
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    #lst.sort()
    return lst

def splitInput(): # data formatting
    busses=[]
    lst = getInput()
    xes = lst[1].split(",")# hehe
    for x in xes:
        if x != "x":
            busses.append(int(x))
    return (int(lst[0]),busses)

def nearestFactor(tup):
    target = tup[0]
    busses = tup[1]
    targetTime = []
    for bus in busses:
        tmp = bus
        while tmp < target:
            tmp = tmp + bus
        total = tmp - target
        targetTime.append((total,bus,tmp))

    #print(targetTime)
    return(target,targetTime)

def findBestTime():
    tup = nearestFactor(splitInput())
    target = tup[0]
    busses = tup[1]
    busses.sort()
    #print(busses[0])
    return busses[0][0]*busses[0][1]

def findConsecutiveTime(sf=1): # this might work, and also might take a REALLY long time to work ? heh
    busses = getInput()[1].split(",") # only part that matters
    offset = int(busses[0])* sf
    found = False
    while not found:
        #print(f" trying {offset}")
        for i,bus in enumerate(busses):
            if bus != "x" and not (offset+i) % int(busses[i]) == 0:
                #print(f"{bus} isn't valid")
                break
        else: # if the entire for-loop completes then it hits this line and returns
            found = True
            return offset
        offset += int(busses[0])
    return -1 # no answer found... this might never run

def lcm(b):
    lcm = 1
    for x in b:
        lcm = lcm*x // gcd(lcm,x)
    return lcm


def findCons(): # this is basically an implementation of the "chineese remainder theorum, which I mostly understand now"
# by far the hardest day so far, had to get a lot of hints
    busses = getInput()[1].split(",")
    b = [] # busses but with correct types...
    for bus in busses:
        if bus != "x":
            b.append(int(bus))
        else:
            b.append("x")
    t = 0 # start at time zero
    matched = [b[0]]
    while True:
        t += lcm(matched)  # increase the check by the lcm of busses that work
        for i, bus in enumerate(b):
            if bus != "x":
                if (t+i) % bus == 0:
                    if bus not in matched: # if a match hasn't been found yet then add it, otherwise its already there
                        matched.append(bus)
        if len(matched) == len(b) - b.count("x"):
            return t

print(findBestTime())
print(findCons())

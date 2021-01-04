import sys
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

def findConsecutiveTime(): # this might work, and also might take a REALLY long time to work ? heh
    busses = getInput()[1].split(",") # only part that matters
    offset = int(busses[0])
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



#print(nearestFactor(splitInput()))
print(findBestTime())
print(findConsecutiveTime())
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


def findCons():
    busses = getInput()[1].split(",")
    b = [] # busses but with correct types...
    for bus in busses:
        if bus != "x":
            b.append(int(bus))
        else:
            b.append("x")
    print(b)
    found = False
    count = 0
#  starting with 7 and 13 7*13 = 91
# and meetingplace1 is 77 ( you find this), then every subsequent meeting place is 77 + (7*13) so 168 is 2nd valid number and so on

    while not found:
        #print(f"{count}")
        if count % b[0] == 0:
            if (count +1) % b[1] == 0:
                print(f"{count} is VALID")
                print({count})
                found = True
        count += b[0]
    found = False
    while not found:
        # check here
        count += (b[0]*b[1])

# this is kind of the general idea, but it has to scale up too 





# so I've done some reading while waiting for this to run ( heh), and I guess
#a) all the bus times are prime, and
#b) because of this there is an algorithmic way to solve it, but I don't know it, and in the discussion it was implied it would be tough to figure out without knowing it.



#print(nearestFactor(splitInput()))
print(findBestTime())
#print(findConsecutiveTime(10000000000000)) # added an offset to near the lower bound to speed things up a *little*
print(findCons())

import sys
def getInput(): # upgraded to take the filename as a parameter for easier testing
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

#print(getInput())

def getSeats(): # this function takes the raw list, and converts it into a coordinate pair of where the seat is
    lst = getInput()
    coord = []
    for seat in lst:
        row = 0
        col = 0
        #print(seat)
        num = ""
        for char in seat[:-3]: # convert the letters into binary
            if char == "B":
                num += "1"
            else:
                num += "0"
        row = int(num,2)# this line converts binary to decimal, very cool python
        num = ""
        for char in seat[-3:]: # this is just a second binary number
            if char == "R":
                num += "1"
            else:
                num += "0"
        col = int(num,2)
        coord.append([row,col])
    return coord

def getSeatId(): # could just call getSeats from here idk
    lst = getSeats()
    ids = []
    for coord in lst:
        ids.append((coord[0]*8) + coord[1])
    return ids

def findMissingId():
    lst = getSeatId()
    lst.sort()
    unmatched = [] # included this instead of returning because the prompt was a bit confusing...
    for ind, entry in enumerate(lst): # looks for an empty seat after a valid seat
        if ind > 1: # the prompt said you're not sitting at the front, so no need to check that one with an edge case.
            if lst[ind-1]+1 != entry:
                unmatched.append(lst[ind-1]+1)
    return unmatched

print(max(getSeatId())) # answer to part 1

print(findMissingId()) # answer to part 2

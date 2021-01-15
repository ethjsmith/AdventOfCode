import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    #lst = [x.strip() for x in lst]
    return lst

# final format should be
# section 1: rules

# section 2: your ticket

# section 3: other tickets

def formatInput():
    out = []
    lst = getInput()
    tmp = []
    for entry in lst:
        if entry == "\n":
            out.append(tmp)
            tmp = []
        else:
            tmp.append(entry.strip())
    out.append(tmp) # get the last section
    return out

def getValid(lst):
    valids = {}
    # rule example "seat: 13-40 or 45-50"
    for rule in lst[0]:

        s = rule.split(": ")[1:] # this is a terrible workaround
        r = s[0].replace(': ',"-").replace(' ','-').split('-') # this is terrible
        #print(f" {r[0]},{r[1]},{r[3]},{r[4]}")
        for x in range(int(r[0]),int(r[1])+1):
            valids[x] = 1
        for x in range(int(r[3]),int(r[4])+1):
            valids[x] = 1
    return valids

def getFailRate():
    fr = []
    lst = formatInput()
    v = getValid(lst)
    for x in lst[2][1:]: # this is so terrible
        r = x.split(",")
        for z in r:
            if int(z) not in v:
                fr.append(int(z))
    return sum(fr)
#print(formatInput())

def removeInvalid():
    lst = formatInput()
    new = []
    v = getValid(lst)
    for x in lst[2][1:]: # this is so terrible
        r = x.split(",")
        for z in r:
            if int(z) not in v:
                break # found an invalid line, so break ?
        else: # if the for terminated correctly
            # didn't find any errors so add this to new
            new.append(x)
    return new

def getValidRanges(lst):
    ranges = []
    valids = {}
    # rule example "seat: 13-40 or 45-50"
    for rule in lst[0]:

        s = rule.split(": ")[1:] # this is a terrible workaround
        r = s[0].replace(': ',"-").replace(' ','-').split('-') # this is terrible
        #print(f" {r[0]},{r[1]},{r[3]},{r[4]}")
        for x in range(int(r[0]),int(r[1])+1):
            valids[x] = 1
        for x in range(int(r[3]),int(r[4])+1):
            valids[x] = 1
        ranges.append(valids)
        valids = {}
    return ranges

def getOrder():
    lst = formatInput() # all input data
    ranges = getValidRanges(lst)
    v = removeInvalid() # valid rules
    for x,piece in enumerate(v):
        tmp = piece.split(',')
        for xx,z in enumerate(tmp):
            tmp[xx] = int(z)
        v[x] = tmp # this whole problem is just formatting data :/
    #print (v)
    #print(ranges)

    # step through each ticket ?
    answer = []
    num = 0

    while num < len(v[0]): # this kind of doesn't work at all, and needs to be broken down into exactly what needs to be checked 
        k = 0
        z =0
        for k, entry in enumerate(v):
            if v[k][z] in ranges[num]:
                continue
            else:
                break
                z += 1
        else:
            answer.append(num)
        num +=1
    return(answer)
print(getFailRate()) # part 1
#print(removeInvalid())
print(getOrder())

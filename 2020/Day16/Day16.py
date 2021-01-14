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
        print(f" {r[0]},{r[1]},{r[3]},{r[4]}")
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



print(getFailRate()) # part 1
print(removeInvalid())

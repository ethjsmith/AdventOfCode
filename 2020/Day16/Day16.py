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

def getUpperLower(lst):
    result = []
    for rule in lst[0]: # this function is JUST as bad as it was the first time ... :)
        s = rule.split(": ")[1:]
        r = s[0].replace(': ',"-").replace(' ','-').split('-')
        result.append([(int(r[0]),int(r[1])),(int(r[3]),int(r[4]))])
    return result

def getOrder():
    lst = formatInput() # all input data
    rng = getUpperLower(lst)
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

    for index,entry in enumerate(rng):
        tkt = v[0]
        #for tkt in v:
            # oh GOD the O(n^3) in three lines! ( it is probably worse with all the other functions leading up to here ... )
        for ind,x in enumerate(tkt):
            print(f"Checking {x} against {entry}")
            if (x >= entry[0][0] and x<= entry[0][1]) or (x >= entry[1][0] and x <= entry[1][1]): # x is valid for the ticket
                print(f"{tkt[ind]} works so checking index: {ind} against others ")
                    # this is a valid range, so check it in the other tickets
                for othertkt in v:
                    if (othertkt[ind] >= entry[0][0] and othertkt[ind]<= entry[0][1]) or (othertkt[ind] >= entry[1][0] and othertkt[ind] <= entry[1][1]):
                        print(f"{othertkt[ind]} works, continuing")
                        continue

                    else:
                        print(f"{othertkt[ind]} DOESN't WOrk for {entry}, moving on")
                        break
                else:
                    print(f"{othertkt[ind]} works(FINAL) so adding that index{ind} because it seems correct? ")
                    answer.append(ind) # maybe ?
                    break
                #else:
                #    break # this is an invalid range for the ticket, and so the ticket is not considered...
            #else: # if x is valid for ALL tickets, then this is right, append it to answer doc
            #    answer.append(index)
    return answer
    # step through each description, and then step through tickets until you find a field that matches all.
    # return that field.

# This day blows ...

# what I should ACTUALLY Do,
# loop through each rules, and find every field that is valid for that field, and from there find a way to map them...
def betterFormat(lst):
    # this formats similar rules together... why tf didn't I do this ?
    result = []
    tmp = []
    for ind,field in enumerate(lst):
        for x in lst:
            tmp.append(x[ind])
        result.append(tmp)
        tmp = []
    return result



def validFields():
    valids = {}
    lst = formatInput()
    rng = getUpperLower(lst)
    v = removeInvalid() # this is kinda dumb too, why is it remaking the lst again ?
    for x,piece in enumerate(v): # why is this HERE
        tmp = piece.split(',')
        for xx,z in enumerate(tmp):
            tmp[xx] = int(z)
        v[x] = tmp
    v2 = betterFormat(v)
    print(v2) # wow

    for z,range in enumerate(rng):
        #print(f"checking against {range}")
        k = True
        for i,index in enumerate(v2):

            for num in index:
                #print(f"checking if {num} valid")
                if (num >= range[0][0] and num <= range[0][1]) or (num >= range[1][0] and num <= range[1][1]): # the check is good
                    #print(f"{num} is valid for {range}")
                    continue
                else:
                    #print("not valid moving on")
                    k = False
                    break

            if k: # if every number in the range was valid, do this
                if i in valids.keys():
                    valids[i].append(z)
                else:
                    valids[i] = [z]
            else:
                k = True



    # for i,index in enumerate(v2):
    #     for num in index:
    #         for range in rng:
    #             if (num >= range[0][0 ]and num <= range [0][1]) or (num >= range[1][0] and num <= range[1][1]): # the check is good
    #                 continue
    #             else:
    #                 break
    #     else: # if every number in the range was valid, do this
    #         if i in valids.keys():
    #             valids[i].append(z)
    #         else:
    #             valids[i] = [z]
    return valids

def getCorrectOrder(): # almost there
    v = validFields()
    print(v)
    answer = {}
    # find every index with only a single option, and remove that from V, and also remove indexes that correlate to that
    while len(answer) < len(v)-1:
        for key in v:
            print(f" {v[key]} and {len(v[key])}")
            if len(v[key]) == 1:
                target = v[key][0]
                answer[key] = target
                print(f" looking for {target} in v")
                for x in v:
                    if target in v[x]:
                        print(f" target {target} found in {v[x]}")
                        v[x].remove(target)
    print(answer)


print(getFailRate()) # part 1
#print(removeInvalid())
#print(getOrder())
#print(validFields())
print(getCorrectOrder())

import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def format():
    l = getInput()
    result = []
    r2 = []
    fin = []
    for line in l:
        r2 = []
        result = line.split(" | ")
        r2.append(result[0].split(" "))
        r2.append(result[1].split(" "))
        fin.append(r2)
    return fin

#print(format())

# the easy segments are
# 1: takes 2 segments
# 4: takes 4 segments ( nice )
# 7: takes 3 segments
# 8: takes 7 segments

def easy(): # part 1, actually not that hard, just ... weird ?
    l = format()
    count = 0 # the result
    for line in l:
        for entry in line[1]:
            if len(entry) == 2 or len(entry) == 4 or len(entry) == 3 or len(entry)==7:
                count += 1
    return count
# the configuration only makes sense this way, somehow that can be used to map this all out ?
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# print(easy())

# 6:0,9,6
# 5: 2,3,5

def populateDict(line):
    mapping = {}
    # loop thru a first time, getting the easy mappings
    l2 = []
    for entry in line:
        if len(entry) == 2:
            mapping[1] = sorted(entry)
        elif len(entry) == 4:
            mapping[4] = sorted(entry)
        elif len(entry) == 7: # what the hell why isn't this firing? am I having a stroke?
            mapping[8] = sorted(entry)
        elif len(entry) == 3:
            mapping[7] = sorted(entry)
        else:
            l2.append(entry)
    l3 = []
    # loop thru a second time getting some harder mappings
    for entry in l2:
        if len(entry) == 6:
            l9 =  all(item in sorted(entry) for item in mapping[4])
            if l9:
                mapping[9] = sorted(entry)
            else:
                l0 =  all(item in sorted(entry) for item in mapping[7])
                if l0:
                    mapping[0] =sorted(entry)
                else:
                    mapping[6] = sorted(entry)
        else:
            l3.append(entry)
    # loop thru a final time getting the hardest mappings
    for entry in l3:
        l3 = all(item in sorted(entry) for item in mapping[1])
        if l3:
            mapping[3] = sorted(entry)
        else:
            l5 = all(item in mapping[6] for item in sorted(entry))
            if l5:
                mapping[5] = sorted(entry)
            else:
                mapping[2] = sorted(entry)

    return mapping

def hard():
    l = format()
    ans = []

    for line in l:
        dic = populateDict(line[0])
        s = ""
        for entry in line[1]:
            for key in dic.keys():
                if sorted(entry) == dic[key]:
                    # we got it
                    #print(f"{key}", end="")
                    s = s + str(key)
                    break
                else:
                    continue # ?
            else:
                print(f"ERROR,{entry} not found")
        ans.append(s)
        print(s)
    return ans
s = hard()
print(s)
sum = 0
for x in s:
    sum += int(x)
print(sum)
# woof 

import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [int(x.strip()) for x in lst]
    return lst

def depthIncrease(f):
    count = 0
    prev = "a"
    for line in f:
        if prev == "a":
            prev = line
        elif line > prev:
            count += 1
            prev = line
        else:
            prev = line
    return count

def slidingWindow(f):
    count = 0
    prev = 'a'
    q = []
    for n in f:
        if len(q) < 3:
            q.append(n)
        #print(q)
        if len(q) == 3:
            total = q[0] + q[1] + q[2]
            #print(total)
            if prev == 'a':
                prev = total
            elif total > prev:
                #print('increased!')
                count += 1
            prev = total
            q.pop(0)
    return count

print(depthIncrease(getInput()))
print(slidingWindow(getInput()))

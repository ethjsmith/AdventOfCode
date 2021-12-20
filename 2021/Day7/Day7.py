import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst
def format():
    l = getInput()
    f = []
    z = l[0].split(",")
    for x in z:
        f.append(int(x))
    return f

#print(format())

def dif(n,n2):
    return abs(n-n2)

def fulldif(n,n2):
    r = abs(n-n2)
    return r * (r+1)/2
def dist(opt=0):
    l = format()
    m = min(l)
    ma = max(l)
    costs = {}
    for depth in range(m,ma):
        costs[depth] = 0 # set up the dict because everything uses a dict LOL
        for crab in l:
            if opt:
                costs[depth] += fulldif(crab,depth)
            else:
                costs[depth] += dif(crab,depth)
    return costs

def ans(part=0):
    if part:
        costs = dist(1)
    else:
        costs = dist()
    lowest = 99999999999999
    ind = 0
    for key in costs.keys():
        if costs[key] < lowest:
            lowest = costs[key]
            ind = key
    print(f"lowest fuel cost is {lowest}, at depth {ind}")

ans()
ans(1)

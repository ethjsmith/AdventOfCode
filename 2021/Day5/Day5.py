import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def format(lst):
    out = []
    for l in lst:
        c = l.split(" -> ")
        #out.append((c[0].split(","),c[1].split(",")))
        c1 = c[0].split(",")
        v1 = []
        for x in c1:
            v1.append(int(x))
        c2 = c[1].split(",")
        v2 = []
        for x in c2:
            v2.append(int(x))
        out.append((v1,v2))
    return out

def map(lst):
    coords = {}
    for pair in lst:
        if pair[0][0] == pair[1][0]: # x coord matches, loop thru y's

            for x in range(min(pair[0][1],pair[1][1]),max(pair[0][1],pair[1][1])+1):
                if (pair[0][0],x) in coords:
                    coords[pair[0][0],x] += 1
                else:
                    coords[pair[0][0],x] = 1
        elif pair[0][0] == pair[0][1]:

            for x in range(min(pair[0][0],pair[1][0]),max(pair[0][0],pair[1][0])+1):
                if (x,pair[0][1]) in coords:
                    coords[x,pair[0][1]] += 1
                else:
                    coords[x,pair[0][1]] = 1
    print(coords)
    return coords

def visualize(c):
    for x in range(0,10):
        for y in range(0,10):
            if (x,y) in c:
                print(c[x,y],end="")
            else:
                print(".",end="")
        print("")


c =map(format(getInput()))
visualize(c)

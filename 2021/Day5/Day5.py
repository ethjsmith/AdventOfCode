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
    #print(out)
    return out

def xmatch(point1,point2):
    if point1[0] == point2[0]:
        return True
    return False
def ymatch(point1,point2):
    if point1[1] == point2[1]:
        return True
    return False

def slope(point1,point2):
    return (point1[1]-point2[1])/(point1[0]-point2[0])
def leftmost(point1,point2): # returns the points, ordered lol
    if point1[0] < point2[0]:
        return point1,point2
    return point2,point1

def map(lst):
    coords = {}
    for pair in lst:
        if xmatch(pair[0],pair[1]):
            #print(f"{pair} is a vertical line")
            for x in range(min(pair[0][1],pair[1][1]),max(pair[0][1],pair[1][1])+1):
                cont = pair[0][0]
                if (cont,x) in coords:
                    coords[cont,x] += 1
                else:
                    coords[cont,x] = 1
        elif ymatch(pair[0],pair[1]):
            #print(f"{pair} is a horz line")
            for x in range(min(pair[0][0],pair[1][0]),max(pair[0][0],pair[1][0])+1):
                cont = pair[1][1]
                if (x,cont) in coords:
                    coords[x,cont] += 1
                else:
                    coords[x,cont] = 1
        else:
            points = leftmost(pair[0],pair[1])
            s = slope(points[0],points[1])
            for x in range(points[1][0]+1-points[0][0]):
                tt = points[0][0] + x,points[0][1] + int(x * s)
                print(tt)
                if tt in coords:
                    coords[tt] += 1
                else:
                    coords[tt] = 1

    return coords

def total(d):
    t = 0
    for v in d.keys():
        if d[v] >= 2:
            t += 1
    return t

def visualize(c):
    for x in range(0,10):
        for y in range(0,10):
            if (y,x) in c:
                print(c[y,x],end="")
            else:
                print(".",end="")
        print("")


c =map(format(getInput()))
#visualize(c)
print(total(c))

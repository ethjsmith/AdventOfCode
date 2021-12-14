import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def position(f):
    coords = [0,0]
    p = f.split(" ")
    #print(p)
    if p[0] == "forward":
        coords[0] += int(p[1])
    elif p[0] == "down":
        coords[1] += int(p[1])
    elif p[0] == "up":
        coords[1] -= int(p[1])
    #print(coords)
    return coords

def parse(f):
    pos = [0,0]
    for line in f:
        p = position(line)
        pos[0] += p[0]
        pos[1] += p[1]
    return pos

def reposition(f,aim):
    coords = [0,0,0]
    p = f.split(" ")
    if p[0] == "forward":
        coords[0] += int(p[1])
        coords[1] += int(p[1]) * aim
    elif p[0] == "down":
        coords[2] += int(p[1])
    elif p[0] == "up":
        coords[2] -= int(p[1])
    return coords

def parse2(f):
    pos = [0,0,0] # depth, horiz, aim
    for line in f:
        p = reposition(line,pos[2])
        pos[0] += p[0]
        pos[1] += p[1]
        pos[2] += p[2]
    return pos

ans = parse2(getInput())
print(ans)
print(ans[0] * ans[1])

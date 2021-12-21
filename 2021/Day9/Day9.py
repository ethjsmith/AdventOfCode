import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def islowest(p,lst):
    # p is (x,y)
    # lst is the grid of coordinates
    x = p[0]
    y = p[1]

    t = int(lst[x][y])
    #print(f"checking {t} ")
    # I feel like there was something very similar to this in last years AOC...
    for z in [-1,1]:
        if x+z >= 0 and x+z < len(lst):
            if int(lst[x+z][y]) <= t:
                return False
        if y+z >= 0 and y+z < len(lst[0]): # this might be right ... I just guessed haha
            if int(lst[x][y+z]) <= t:
                return False
    return True # this is the lowest point around, very cool

def sumrisklevel():
    l = getInput()
    lowests = []
    total = 0
    for i in range(len(l)):
        for j in range(len(str(l[0]))):
            if islowest((i,j),l):
                lowests.append(l[i][j])
                total = total + int((l[i][j]))+1
    print(lowests)
    return total;

#print(sumrisklevel()) # part 1

def basin(p,lst,ind):
    x = p[0]
    y = p[1]
    t = int(lst[x][y])
    for z in [-1,1]:
        if x+z >= 0 and x+z < len(lst):
            if int(lst[x+z][y]) > t and int(lst[x+z][y]) < 9:
                basin((x+z,y),lst,ind)
        if y+z >= 0 and y+z < len(lst[0]): # this might be right ... I just guessed haha
            if int(lst[x][y+z]) > t and int(lst[x][y+z]) < 9:
                basin((x,y+z),lst,ind)
    ind[(x,y)] = 1 # why is the solution ALWAYS a dictionary ...


def basinfinder(): # please stop, you're killing him !
    l = getInput()
    sizes  = []

    for i in range(len(l)):
        for j in range(len(str(l[0]))):
            ind = {}
            if islowest((i,j),l):
                basin((i,j),l,ind)
                sizes.append(len(ind.keys()))
                print(len(ind.keys()))
    print(sorted(sizes))
    return sorted(sizes)
z = basinfinder()
sum = 1
for x in z[-3:]:
    sum *= x
print(sum)

import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def model(lst,threshold,version=1):
    #print(*lst, sep = "\n")
    #print("  ")
    #lst = getInput()
    # how to traverse this?
    newlst = []
    for y, s in enumerate(lst):
        tmp = ""
        for x, seat in enumerate(s): # nested for to loop through each character
            count = 0
            #tmp = ""
            if seat != ".":
                if version == 1:
                    count = checkAdjacent(x,y,lst)
                else:
                    count = checkAdjacent2(x,y,lst)
                #print(f"for coordinate {x} {y} count is : {count}")
                #tmp += "."
            if seat == "L":
                if count == 0:
                    tmp += "#"
                else:
                    tmp += "L"
            elif seat == "#":
                if count >= threshold:
                    tmp += "L"
                else:
                    tmp += "#"
            else:
                tmp += "."
        newlst.append(tmp)
    print(*newlst, sep="\n")
    print(" ")
    return newlst

def checkAdjacent(x,y,lst): # I messed up the variable orders, and fixed it by swapping the variables instead of something cleaner
                            # so this basically makes no sense
    count = 0
    #for item in (lst[y-1][x-1],lst[y-1][x],lst[y-1][x+1],lst[y][x-1],lst[y][x+1],lst[y+1][x-1],lst[y+1][x],lst[y+1][x+1]):
    checks = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    #print(checks)
    for xx,yy in checks:
        #print(f"{xx},{yy}")
        if (xx +y < len(lst) and yy + x < len(lst[0]) and xx+y >= 0 and yy+x >= 0):
            #print(f"{lst[xx+y][yy+x]} at ({xx+y},{yy+x})")
            if lst[xx+y][yy+x] == "#":
                count += 1
    return count

def checkAdjacent2(x,y,lst):
    count = 0
    checks = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    for xx,yy in checks:
        tx=xx
        ty=yy
        #print(f"{xx},{yy}")
        while (tx +y < len(lst) and ty + x < len(lst[0]) and tx+y >= 0 and ty+x >= 0):
            #print(f"{lst[tx+y][ty+x]} at ({tx+y},{ty+x})")
            if lst[tx+y][ty+x] == "#":
                count += 1
                break
            elif lst[tx+y][ty+x] == "L":
                break
            else:
                tx += xx
                ty += yy
    return count


def findEndState(t,v=1):
    #tmp = getInput()
    tmp = model(getInput(),t,v)
    tmp2 = model(tmp,t,v)
    while True:
        if tmp == tmp2:
            print('found equilibrium')
            #return tmp
            # count the seats
            count = 0
            for row in tmp2:
                for letter in row:
                    if letter == "#":
                        count += 1
            return count
        else:
            tmp = tmp2
            tmp2 = model(tmp2,t,v)
            #print(tmp)

#print(findEndState(4)) # Part 1
print(findEndState(5,2)) # Part 2
# not 2575

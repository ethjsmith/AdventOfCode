import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def model(lst):
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
                count = checkAdjacent(x,y,lst)
                print(f"for coordinate {x} {y} count is : {count}")
                #tmp += "."
            if seat == "L":
                if count == 0:
                    tmp += "#"
                else:
                    tmp += "L"
            elif seat == "#":
                if count >= 4:
                    tmp += "L"
                else:
                    tmp += "#"
            else:
                tmp += "."
        newlst.append(tmp)
    print(*newlst, sep="\n")
    print(" ")
    return newlst

def checkAdjacent(x,y,lst):
    count = 0
    #for item in (lst[y-1][x-1],lst[y-1][x],lst[y-1][x+1],lst[y][x-1],lst[y][x+1],lst[y+1][x-1],lst[y+1][x],lst[y+1][x+1]):
    checks = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    for xx,yy in checks:
        if (xx +x <= len(lst) and yy + y <= len(lst[0]) and xx+x >= 0 and yy+y >= 0):
            if lst[xx][yy] == "#":
                count += 1
    return count


def findEndState():
    #tmp = getInput()
    tmp = model(getInput())
    tmp2 = model(tmp)
    while True:
        if tmp == tmp2:
            print('found equilibrium')
            #return tmp
            # count the seats
            count = 0
            for row in tmp2:
                for letter in row:
                    if letter == "L":
                        count += 1
            return count
        else:
            tmp = tmp2
            tmp2 = model(tmp2)
            #print(tmp)

print(findEndState())

import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

# heh, one liner input

def playGame(tns):
    lst = getInput()[0].split(",") # should be one line only
    turns = {}
    turncounter = 0
    while turncounter < tns:
        print(turns)
        if turncounter < len(lst): # read in the first three turns
            turns[int(lst[turncounter])] = turncounter
            prev = lst[turncounter]
            print(f"Turn {turncounter+1} : {prev}")
        else:
            if prev in turns:
                turns[int(turns[prev])] = (turncounter-1)-turns[prev]
                prev = turns[prev] # ? like this ?

            else:
                turns[0] = turncounter
                prev = 0
            print(f"Turn {turncounter+1} : {prev}")
        turncounter += 1
    print(turns)
print(playGame(10))

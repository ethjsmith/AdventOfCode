# NOT 37
import sys, re
global acc
acc = 0 # accumulator

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

# am I really gonna use a dict for every problem in this challenge?

# yes

def findLoop(lst):# passing it in, bc I want to change it for part 2
    global acc
    #lst = getInput()
    #for i, cmd in enumerate(lst):
    i =0
    visited = {"-1"}
    while True: # im getting flashbacks to last years challenges ...  monka
        tmp = visited.copy()
        tmp.add(i) # add i to the set of instructions that have been accessed ... this might work ?
        #print(tmp)
        #print(visited)
        if tmp == visited:
            print("loop found")
            return 1 # if we hit a loop, return the value in the register... (BEFORE THE LOOP DAMNIT)
        else:
            visited = tmp
        if i >= len(lst): # catch for no loop, or success
            print("successful termination")
            return 0 # I dunno, returning something other than a number indicates success... that's dumb
        print(lst[i][:3])

        if lst[i][:3] == "nop":
            i+= 1
        elif lst[i][:3] == "acc":
            if lst[i][4] == "+":
                acc += int(lst[i][5:])
            else:
                acc -= int(lst[i][5:])
            i += 1
        elif lst[i][:3] == "jmp":
            if lst[i][4] == "+":
                i += int(lst[i][5:])
            else:
                i -= int(lst[i][5:])
        else:
            print("error")
            break
def changeindex(): # changes an index, and then checks for a loop
    global acc
    master = getInput()
    #for entry in master:
    for i, entry in enumerate(master):
        acc = 0
        if entry[:3] == "nop":
            master[i] = "jmp" + entry[3:]
            if findLoop(master) == 0:
                return acc
            else:
                master[i] = "nop" + entry[3:]
        elif entry[:3] == "jmp":
            master[i] = "nop" + entry[3:]
            if findLoop(master) == 0:
                return acc
            else:
                master[i] = "jmp" + entry[3:]



findLoop(getInput())
print(acc) # this gives the results for part 1, ( modified slightly from original code to continue to work during p2 construction)

print(changeindex()) # results for part 2

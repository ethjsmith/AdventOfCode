# wtf is this input... 
def getInput(y ,path="2022/Day5/"):
    with open(f"{path}{y}.txt") as f:
        lst = f.readlines()
    stacks= {}
    for x in lst:
        if x =="\n": # heh
            break
        for i in enumerate(x):
            # print(i)
            if i[0] not in stacks:
                stacks[i[0]] = i[1]
            else:
                stacks[i[0]] = stacks[i[0]] + i[1]
    new = {} # ok I have partially formatted half of the puzzle... 
    for item in stacks.keys():
        # print(stacks[item][-1])
        if stacks[item][-1].isdigit():
            new[stacks[item][-1]] = stacks[item][:-1].strip()[::-1] # I probably should have just used regex?
    for item in new.keys():
        new[item] = [*new[item]]
    midpoint = False
    newlist = []
    for x in lst:
        if midpoint:# yeah I definitely should've started with re 
            bull = x.split(" from ")
            shit = bull[1].strip().split(" to ")
            newlist.append([int(bull[0][5::]),int(shit[0]),int(shit[1])]) # in hindsight, terrible naming convention :) 
        if x =="\n":
            midpoint = True
    return(new, newlist) 

def followInstructions(stacks,instructions):
    # 0 = # of times, 1 = from, 2= destination
    for line in instructions:
        for num in range(0,line[0]):
            a = stacks[str(line[1])].pop()
            stacks[str(line[2])].append(a)
    return stacks

# part 2
def followInstructionsAgain(stacks,instructions):
    for line in instructions:
        # I literally switched my thing from lists to strings to make part 1 easier, and boom, part 2 is harder :/ 
        a = stacks[str(line[1])][line[0]*-1:]
        stacks[str(line[1])] = stacks[str(line[1])][:line[0]*-1]
        stacks[str(line[2])] = stacks[str(line[2])] + a
        # a = stacks[str(line[1])]
    return stacks

def topofeach(s):
    _str = ""
    for x in s.keys():
        _str += s[x].pop()
    return _str

# print(getInput("example"))

a,b = getInput("input")
z = followInstructions(a,b)
# zz = followInstructionsAgain(a,b)
# whoops, forgot that I'm mutating the dicts, gotta just run it again
print(topofeach(z))

c,d = getInput("input")
zz = followInstructionsAgain(c,d)
print(topofeach(zz))
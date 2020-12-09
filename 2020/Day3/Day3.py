def getInput(fname):
    with open(fname) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

# def parseToArray(lst):
#     field = [][]
#     for line in lst:
#         for char in line:
            # hmm with python I maybe don't need to do this ...

def hitTrees(l,itr,d=1): # l is the input, itr is how far right you move every action, and d is lines down
    hits = 0
    pos = 0
    tempd = d
    iterl = iter(l) # skip the first line
    next(iterl)
    for line in iterl:

        if (tempd > 1):
            tempd -=1
        else:
            pos +=itr
            if pos >= len(line):
                pos -= len(line)
            if line[pos] == "#":
                hits += 1
            tempd = d
    return hits

ans = 1
ans = ans * hitTrees(getInput('input.txt'),1)
ans = ans * hitTrees(getInput('input.txt'),3)
ans = ans * hitTrees(getInput('input.txt'),5)
ans = ans * hitTrees(getInput('input.txt'),7)
ans = ans * hitTrees(getInput('input.txt'),1,2)

print(ans)

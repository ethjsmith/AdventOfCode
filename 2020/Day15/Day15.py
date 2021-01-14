import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

# heh, one liner input
def play(t):
    lst = getInput()[0].split(",")
    for n,x in enumerate(lst): # convert all datatypes to int
        lst[n] = int(x)
    turns = {}
    counter = 0
    prev = 0
    for x in lst: # initalize the puzzle input
        turns[x] = [counter]
        counter += 1
        prev = x
    while counter < t: # in this section the goal is to find the number to be spoken
        if prev in turns and len(turns[prev]) > 1:
            new = turns[prev][len(turns[prev])-1] - turns[prev][len(turns[prev])-2]
            if new in turns:
                turns[new].append(counter)
            else:
                turns[new] = [counter]
            prev = new
        else:
            turns[0].append(counter)
            prev = 0
        counter += 1
        #print(f" Turn{counter}: {prev}")
    print(turns)
    return prev
print(play(2020)) # part 1
print(play(30000000)) # part 2? slow, but no change needed?
# I love computers

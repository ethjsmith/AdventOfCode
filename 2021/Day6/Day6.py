import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def format():
    l2 = []
    l =getInput()[0].split(",")
    for entry in l:
        l2.append(int(entry))
    return l2

#print(format())

def simulate(l):
    new = []
    remake = []
    for fish in l:
        r = fish - 1
        if r < 0:
            new.append(8)
            r = 6
        remake.append(r)
    return remake + new

def go(days):
    fish = format()
    while days > 0:
        #print(fish)
        fish = simulate(fish)
        days -= 1
    print(len(fish))

def f2():
    ages = {
    0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0
    }
    l = format()
    for age in l:
        ages[age] += 1
    return ages

def simul8(l):
    tmp = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

    for t in l.keys():
        if t == 0:
            tmp[8] += l[t]
            tmp[6] += l[t]
        else:
            tmp[t-1] += l[t]
    return tmp
    # tries to simulate... 8 days at a time? or something idk haha
    # is it dict time? it seems like it always is

#go(80) # part 1 lol
def go2(days):
    fish = f2()
    while days > 0:
        fish = simul8(fish)
        days -= 1
    total = 0
    for key in fish.keys():
        total += fish[key]
    print(total)

go2(256) # part 2 :)
# good one :) 

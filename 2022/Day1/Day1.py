import sys

def getInput(y):
    with open(y) as f:
        lst = f.readlines()
    master = []
    minion = []
    for x in lst:
        if x == "\n":
            master.append(minion)
            minion = []
        else:
            minion.append(int(x.strip()))
    return master

def calories(l):
    elves = []
    total = 0
    for elf in l:
        for x in elf:
            total += x
        elves.append(total)
        total =0
    return(elves)

def find_top(l):
    max=  0
    for x in l:
        if x > max:
            max = x
    return max



def top3(l ,times= 3):
    tops = []
    for x in range(0,times):
        tmp = find_top(l)
        tops.append(tmp)
        l.remove(tmp)
    return tops

print(calories(getInput("2022/Day1/test.txt")))

cal = calories(getInput("2022/Day1/input.txt"))
print(find_top(cal))

zoom = top3(calories(getInput("2022/Day1/input.txt")))
print (zoom)
tota = 0
for x in zoom:
    tota += x
print (tota)

# this is a mess LOL 
# like this is genuinely terrible code and I am somewhat embarrased to push it to github in this state... I should come back and fix it :) probably I wont tho 
import math
#day1 part 1
def getFuel(inp):
    return math.floor(inp/3)-2

#print(getFuel(100756))

def sum():
    f = open('input.txt', "r")
    total =0
    for line in f:
        total += getFuel(int(line))
    return total

print(sum())


#day1 part2

def sumWithFuel():
    f = open('input.txt', "r")
    total =0
    for line in f:
        addedToAdded = 0
        addedFuel = getFuel(int(line))
        addedToAdded = getFuel(addedFuel)
        while(addedToAdded > 0):
            total += addedToAdded
            addedToAdded = getFuel(int(addedToAdded))
        total += addedFuel
    return total



print(sumWithFuel())

import sys

# formatting in the getInput function this year? 
def getInput(y ,path="2022/Day3/"):
    with open(f"{path}{y}.txt") as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    newlist= []
    for line in lst:
        n = len(line) //2
        # print(n)
        newlist.append((line[0:n], line[n:]))
    return newlist

#print(getInput("example"))
def value(char):
    # a-z = 1-26 A-z = 27-52
    # in ascii these characters are also sequential so we just gotta do some math to get our correct values? 
    if char.isupper():
        # ascii A = 65
        return ord(char) - 38
    # ascii a = 97 so
    return ord(char)- 96 

def findWrongCharacter(a,b):
    in_a = {}
    for char in a:
        in_a[char] = 1
    for char in b:
        if char in in_a:
            return char
    print("error?")
    
def drive(z):
    l = getInput(z)
    chars = []
    for line in l:
        chars.append(findWrongCharacter(line[0],line[1]))
    total = 0
    for x in chars:
        total += value(x)
    return total
# part 1
print(drive("input"))

# I hate when part 2 gets more complicated ( every time )
def find_badge_type(abc):
    # takes three elves bags, and finds the item that is shared between each of them 
    items = {}
    for elf in abc:
        e = {}
        for compartment in elf: # for x in 2 hehe
            for item in compartment: # LOL this is so scuffed 
                e[item] = 1  
        items[elf] = e
    # I LOVE DICTS I LOVE DICTS 
    for item in items[abc[0]]:
        if item in items[abc[1]] and item in items[abc[2]]:
            return item
    print("error?")

def drive2(z):
    l = getInput(z)
    badges = []
    for i in range(0,len(l),3):
        x = (l[i],l[i+1],l[i+2])
        badges.append(find_badge_type(x))
    total = 0
    for x in badges:
        total += value(x)
    return total
# Part 2 
print(drive2("input"))
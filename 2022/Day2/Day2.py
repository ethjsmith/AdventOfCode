import sys

# I would like to scrape right off the web, but oauth2 is kind of complicated and Im doing this more for fun than to ... learn heehee
def getInput(y):
    with open(y) as f:
        lst = f.readlines()
    lst = [(x[0], x[2]) for x in lst]
    return lst

#print(getInput("2022/Day2/example.txt")) # why is it thinking this way what is going on?

scores = {
    'X':1, # Rock       A
    'Y':2, # Paper      B
    'Z':3, # Scissors   C
    'A':1, # ROCK       x :/
    'B':2, # PAPER      y
    'C':3, # SCISSORS   z
}

def normalize(elf):
    if elf == "A":
        return "X"
    if elf =="B":
        return "Y"
    return "Z"

def calc_win_score(elf,you): # maybe? 
    elf = normalize(elf)
    if elf == you: # draw 
        return 3
    if elf != you:# not draw
        if elf =="X":# Rock
            if you == "Y":
                return 6
            return 0
        if elf =="Y":# Paper
            if you =="Z":
                return 6
            return 0
        if elf =="Z":
            if you =="X":
                return 6
            return 0

def calculate(l = getInput("2022/Day2/input.txt")):
    total_score = 0
    for round in l:
        #print(round)
        z = calc_win_score(round[0],round[1])
        #print (z)
        total_score += z # score for winning
        total_score += scores[round[1]] # score for playing a certain thing
    return total_score

print(calculate())

# that was part 1, but part 2 is very different ... damn 
# A lot of this stuff feels like it's trying to teach code re-use and modularability and I just mess it up every time
# maybe that's just me projecting other stuff that I'm thinking about elsewhere ... 

win = {
   "A":"B",
   "B":"C",
   "C":"A",
}
lose ={
    "A":"C",
    "B":"A",
    "C":"B",
}

def calc_score_per_round(elf,you):
    # maybe some kind of linked list that points to "next or prev or somehting haha "
    # oh that would work actually lol 
    if you == "X": # lose
        s = 0 +scores[lose[elf]]
    if you =="Y": # Draw
        s = 3 + scores[elf]
    if you == "Z": # win 
        s = 6 + scores[win[elf]] 
    return s

def calculate2(l = getInput("2022/Day2/example.txt")):
    total=  0
    for x in l:
        total += calc_score_per_round(x[0],x[1])
    return total

# ok so my part2 code was actually much cleaner, I think I just GOT it, and going back I could've made part 1 better too? 
# ( TO be fair I do ahve a couple dicts that are ugly ... but I think that's fine, )
print(calculate2())
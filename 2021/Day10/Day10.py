import sys

scores = { # is this global? lol
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}
s2 = { # lol
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def check(a,b):
    if a == "(":
        if b == ")":
            return True
        else:
            return False
    elif a == "<":
        if b == ">":
            return True
        else:
            return False
    elif a == "{":
        if b == "}":
            return True
        else:
            return False
    elif a == "[":
        if b == "]":
            return True
        else:
            return False
    return "error lol ?"
def checkline(line):
    ll = [] # line stack
    for char in line:
        if char in ("{","(","[","<"):
            ll.append(char)
        elif char in ("}",")","]",">"):
            if check(ll[-1],char):
                ll.pop()
            else:
                return scores[char]
    return 0


def checkline2(line):
    ll = [] # line stack
    for char in line:
        if char in ("{","(","[","<"):
            ll.append(char)
        elif char in ("}",")","]",">"):
            if check(ll[-1],char):
                ll.pop()
            else:
                return -1
    return ll
def removecorrupted(): # removes the corrupted lines
    l = getInput()
    new = []
    for line in l:
        r = checkline2(line)
        if r != -1:
            new.append(r)
    return new

def corrupted(): # this is a stack thing for sure

    l = getInput()
    score = 0
    ex = ""
    prev = ""
    ll = []
    for line in l:
        score += checkline(line)
    print(score)

#corrupted() # part 1

def findmissing():
    scores = []
    l = removecorrupted()
    for line in l:
        score = 0
        for char in line[::-1]: # lol ok yeah
            # how annoying
            score *= 5
            if char == "(":
                score += s2[")"]
            elif char == "{":
                score += s2["}"]
            elif char == "[":
                score += s2["]"]
            elif char == "<":
                score += s2[">"]
            else:
                print("ERROR LOL")
        scores.append(score)
    return scores
def final():
    l = findmissing()
    l.sort()
    return l[len(l)//2]
print(final())

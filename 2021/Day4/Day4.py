import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

# umm... wow
def format(lst):
    numbers =lst.pop(0)
    lst.pop(0) # remove the first newline line
    cards = []
    card = [] # the depth we're about to go to ...
    for line in lst:
        #print(line)
        if line == "":
            cards.append(card)
            card = []
        else:
            card.append(line)
    cards.append(card)
    #print(numbers)
    numbers = numbers.split(",")
    r = []
    for n in numbers:
        r.append(int(n))
    #print(cards)
    allcards = []
    for singlecard in cards: # this is a weirdly formatted string
        newcard = []
        for line in singlecard:
            l = line.split()
            newline = []
            for num in l:
                newline.append([int(num),0])
            newcard.append(newline)
        allcards.append(newcard)
    return(allcards,r) # woof

def check(lst):
    # checks a list to see if it has won
    # oh my god, are we going deeper?
    for line in lst: # the easy check
        #print(f"checking {line}")
        for x in line:
            #print(x)
            if x[1] == 1:
                continue # has been picked, keep checking
            else:
                break #hasn't been picked, this isn't a win
        else: # I think ?
            return True # this one wins
    for x in range(len(lst[0])):
        for line in lst: # maybe? holy shit this is like
            #print(f"checking {line[x]}")
            if line[x][1] == 1:
                continue
            else:
                break
        else:
            return True # wins on horizontal
    return False # no win condition found so no win
    # wow, the average case for this function is REALLY high

def game(cards,numbers):
    for n in numbers: # draw a number
        #print(f"drawing {n}")
        for card in cards: # oh my  we're going so deep, there should be a dictionary somewhere in this trash ...
            for line in card:
                for num in line: # HAHAHAHHAHAHAHAHAHAHAHAHAHa
                    if num[0] == n:
                        num[1] = 1
            if check(card):
                return answer(card,n)

    else:
        print("no winner probably bugged?")
        return -1

def lastgame(cards,numbers):
        for n in numbers: # draw a number
            #print(f"drawing {n}")
            for card in cards:
                for line in card:
                    for num in line:
                        if num[0] == n:
                            num[1] = 1
            for card in cards:
                if check(card):# if this card is a winner,
                    print(answer(card,n)) # calculate and print the answer,
                    #print(f"removing {card}")
                    cards.remove(card) # and remove the winning card from the loop
                    print(f"lenth:{len(cards)}")

def answer(lst,last): # takes the winning list, and final called number, and outputs the result
    #print(f"lst: {lst}, and last: {last}")
    total = 0
    for line in lst:
        for entry in line:
            if entry[1] == 0:
                total += entry[0]
    return total * last

z = format(getInput())
#print(z)
print(f" game 1 winner score: {game(z[0],z[1])}")
print("---")
k = format(getInput())
print(lastgame(k[0],k[1]))
# 16432 too low

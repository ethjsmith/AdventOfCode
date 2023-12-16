
def getInput(file):
    with open(file) as f:
        lines = [l.strip() for l in f]
    return lines


def format_cards(file):
    new = []
    for line in file:
        a = line.split("|")
        winners = [int(x) for x in a[0].split(":")[1].split(" ") if x != ""]
        owned = [int(x) for x in a[1][1:].split(" ") if x != ""]
        # I swear I write at least one function like this every year, and it makes me sick
        new.append((set(winners),set(owned)))
    return new
    
file = getInput("2023/Day4/input.txt")
formatted = format_cards(file)

def determine_score(card):
    score = len(set.intersection(card[0], card[1]))
    if score > 0:
        return 2 ** (score-1) 
    else:
        return 0
scores = []
for card in formatted:
    scores.append(determine_score(card))
# part 1 :^)    
# print(scores)    
print(sum(scores))

# PART 2
 
# runs = []
# newruns = []
# for x in range(0,len(formatted)):
#     runs.append(0) # set all to zero 
#     newruns.append(0)
# print("a")
# for x in range(len(formatted)):
#     s = determine_score(formatted[x])
#     for z in range(0,s):
#         # print(f"{x+z}, {newruns[x+z]}")
#         newruns[x+z] = newruns[x+z] + 1
def determine_score2(card):
    # I am fucking dumb 
    return len(set.intersection(card[0], card[1]))
# OK FOR REAL LOL
cards = {}
for x in range(len(formatted)):
    cards[x] = 1
    
for x in range(len(formatted)):
    score = determine_score2(formatted[x])
    for z in range(1,score+1):
        cards[x+z] += cards[x]
        
print(cards)
# numbered = []
# for x in range(len(formatted)):
#     numbered.append((x,formatted[x],1))

# for card in numbered:
#     card_score = determine_score(card[1])
#     for x in range(1,card_score):
#         numbered[]
        
        
        
# def do_the_thing(formatted):
#     runs = [1]
#     for x in range(0,len(formatted)-1):
#         runs.append(0)
#     for x in range(len(formatted)):
#         score = determine_score(formatted[x])
        
    # need too loop over the list, once
    # and increment a counter for each card based on it's results I think
{1,2,4,8,14,1}
print(sum(cards.values()))
# def determine_score2(card, runs):
#     score = len(set.intersection(card[0], card[1]))
     
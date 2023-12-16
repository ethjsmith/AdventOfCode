
def getInput(file):
    with open(file) as f:
        lines = [l for l in f]
    return lines

def format(file):
    hands = []
    for line in file:
        sections = line.split(" ")
        # I think I don't actually want the first part to be a string, I want like a dict or something
        di = {}
        for char in sections[0]:
            if char in di.keys():
                di[char] += 1
            else:
                di[char] = 1
        # need all 3 I htink for ties        
        hands.append((di,sections[0], int(sections[1])))
    return hands

print(format(getInput("2023/Day7/example.txt")))


# I think I will write many helper functions? idk 

def is_x(x,num): # this can find 5x, 4x, 3x, and 2x
    for key in x.keys():
            if x[key] == num:
                return True
        return False
def full_house(x):
    # for it to be fh there can only be a 3 and a 2
    if len(x.keys()) == 2:
        # LOL 
        if (x[x.keys()[0]] == 2 and x[x.keys()[1]] == 3) or (x[x.keys()[1]] == 2 and x[x.keys()[0]] == 3):
            return True 
    return False
def two_pair (x):
    num_pairs = 0
    for z in x.keys():
        if x[z] == 2:
            num_pairs += 1 
    if num_pairs == 2:
        return True 
    return False 
def high_card(x): # maybe don't need, like this is the "except?"
    if len(x.keys()) == 5:
        return True 
    return False 
# HAHAHAHAHAHAHAHAHAHAHAHA
def score(a):
    if is_x(a,5):
        return 7
    if is_x(a,4):
        return 6
    if full_house(x):
        return 5
    if is_x(a,3):
        return 4
    if two_pair(x):
        return 3
    if is_x(a,2):
        return 2
    return 1 # yeah don't need high card :)
# hmm now that I am done sorting these bad boys, this is suddenly a sorting algo... die please           
# I think I can write a comparison and then let python list.sort() do it iirc 
def tiebreaker(a,b):
    powers = ["A","K", "Q", "J", "T", "9",'8','7','6','5','4','3','2']
    for i in range(len(a)):
        
def compare_hands(a,b):
    score_a = score(a)
    score_b = score(b)
    if score_a == score_b:
        tiebreaker(askldjalksjdlajsldkjalsdjalk)
    return score_a - score_b
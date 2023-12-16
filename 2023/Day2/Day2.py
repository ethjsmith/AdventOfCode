import re

def getInput(file):
    with open(file) as f:
        lines = [l for l in f]
    return lines

day1 = [12,13,14] # rgb
# or
da1 = {
    "red":12,
    "green":13,
    "blue":14
}

def format(line):
    ret = []
    l = line.split(":")[1]
    l = l.split(';')
    # print(l)
    # for pull in game 
    for x in l:
        pulls = re.findall(r"\d* (?:green|red|blue)", x)
        formatted = {"red":0,"green":0,"blue":0}
        for color in pulls:
            if "red" in color: # this can be better ? 
                formatted["red"] = int(color.split(" ")[0])
            elif "blue" in color:
                formatted["blue"] = int(color.split(" ")[0])
            elif "green"in color:
                formatted["green"] = int(color.split(" ")[0])
        ret.append(formatted)
    return ret
        
def valid_games(games):
    # return the ID of each valid game
    # I hate this 
    g= 0
    for x in range(len(games)):
        if game_is_valid(games[x],da1):
            g += x+1
    print(f"part 1: {g}")

def game_is_valid(game: dict, stats: dict):
    for throw in game:
        for key in stats.keys():
            if throw[key] > stats[key]:
                return False
    return True
allgames= []
for l in getInput("2023/Day2/input.txt"):
    allgames.append(format(l))
valid_games(allgames)

# part 2 :^)
def least_possible(game):
    least = {"red":0,"green":0,"blue":0}
    for throw in game:
        for key in throw.keys():
            if throw[key] > least[key] and throw[key] != 0:
                least[key] = throw[key]
    return least

def power(g):
    a = 1
    for x in g.keys():
        a = a * g[x]
    return a

least_all = []
for game in allgames:
    least_all.append(least_possible(game))

sum = 0
for x in least_all:
    sum += power(x)
print(f"Part 2: {sum}")



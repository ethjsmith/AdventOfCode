import re 

def getInput(file):
    with open(file) as f:
        lines = [l for l in f]
    return lines

def format(file):
    # these puzzles where inputs are all in 1 line are kinda annoying I gotta say. I just wanna 
    # loop thru the thing :^~o
    # I will instead be lazy by using regex :) 
    times = re.findall("\d+", file[0])
    distances = re.findall("\d+", file[1])
    races = []
    for i in range(len(times)):
        races.append((int(times[i]),int(distances[i])))
    return races
races = format(getInput('2023/Day6/input.txt'))
    

def calc_acceleration(a,rem):
    # this doesn't need to be a function lol
    return a * rem 

def do_something(race):
    # idk calculate the things or something 
    times = []
    for x in range(0,race[0]): # all possible times in a race
        time = calc_acceleration(x,race[0]-x)
        if time > race[1]:
            times.append(time)
    return times # I guess just count here for puzzle 1 ? 

# print(do_something(races[0]))

def numba_one(races):
    total = 1
    for race in races:
        total *= len(do_something(race))
    return total
# part 1 
print(numba_one(races))

# lol I figured looking at this that this was gonna be a case of > efficent solution > inefficent part 2

def format_again(file):
    times = re.findall("\d+", file[0])
    distances = re.findall("\d+", file[1])
    time = ""
    dist = ''
    for x in range(len(times)):
        time += times[x]
        dist += distances[x]
    return (int(time),int(dist))
        
ultra_race = format_again(getInput('2023/Day6/input.txt'))
# maybe my computer is just really good, but using the old engine, it only took about 10 seconds...
# so chalk that one up as a win :) 
print(len(do_something(ultra_race)))
# update I went and checked AOC reddit, and yeah that wasn't the intended solution.
# I am not fixing it, this is supposed to be fun, and my iterative solution beating it was FUN 
# ( also things being for fun is why my code looks so bad, I promise)
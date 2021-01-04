import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    #lst.sort()
    return lst

# ship starts facing "east " ->
# seems to start at 0,0
def trackship():
    position = [0,0]
    # N = 0 or 360
    facing = 90 # this is East
    lst = getInput()
    for instruction in lst:
        direction = instruction[0]
        # first character
        if direction == "N":
            position[0] += int(instruction[1:])
        elif direction == "S":
            position[0] -= int(instruction[1:])
        elif direction == "E":
            position[1] += int(instruction[1:])
        elif direction == "W":
            position[1] -= int(instruction[1:])
        elif direction == "L":
            facing -= int(instruction[1:])
            if facing < 0:
                facing += 360
        elif direction =="R":
            facing += int(instruction[1:])
            if facing >= 360: # what if it goes super negative?
                facing -= 360
        elif direction == "F":
            if facing == 0 or facing == 360:
                position[0] += int(instruction[1:])
            elif facing == 90:
                position[1] += int(instruction[1:])
            elif facing == 180:
                position[0] -= int(instruction[1:])
            elif facing == 270:
                position[1] -= int(instruction[1:])
            else:
                print(f"Error with facing {instruction}")
                break
        else:
            print(f"error!!{instruction}:::{direction}")
            break
    return position

def trackBeacon():
    lst = getInput()
    position = [0,0]
    waypoint = [1,10]
    for instruction in lst:
        #print(f"POS:{position}, WAY:{waypoint}")
        direction = instruction[0]
        if direction == "N":
            waypoint[0] += int(instruction[1:])
        elif direction == "S":
            waypoint[0] -= int(instruction[1:])
        elif direction == "E":
            waypoint[1] += int(instruction[1:])
        elif direction == "W":
            waypoint[1] -= int(instruction[1:])
        # the harder(?) part
        elif direction == "L" or direction == "R":
            if direction == "L": # haha this is bad
                l = 1
                r = -1
            else:
                l = -1
                r = 1
            depth = int(instruction[1:])
            if depth == 0 or depth == 360: # do nothing haha
                print("im doing nothing rn ") #
            elif depth == 90:
                tmp = waypoint[0] # :(
                waypoint[0] = waypoint[1]
                waypoint[1] = tmp
                waypoint[0] = waypoint[0] * l
                waypoint[1] = waypoint[1] * r
            elif depth == 180:
                waypoint[0] = waypoint[0] * -1
                waypoint[1] = waypoint[1] * -1
            elif depth == 270:
                tmp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = tmp
                waypoint[0] = waypoint[0] * r
                waypoint[1] = waypoint[1] * l
            else:
                print(f"ERROR :::{instruction}")
            # how to rotate a coordinate exactly 90 degrees
        elif direction == "F":
            times = int(instruction[1:])
            while times > 0:
                position[0] += waypoint[0]
                position[1] += waypoint[1]
                times -= 1
        else:
            print(f"Error :{direction}")
    return position

def manhattanDistance(lst): # quality function kek
    return abs(lst[0]) + abs(lst[1])

#print(trackship())
print(manhattanDistance(trackship()))
print(manhattanDistance(trackBeacon()))

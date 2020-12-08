import math
# O(N^2) so it's really slow, and bad, but I couldn't think of a better way to do it off the top of my head :/
# actually this might be n^3 :( 
def proj():
    f = open('input.txt', 'r')
    both =[]
    for line in f:
        commands = line.split(",")
        positions =[]
        x=0
        y=0
        #0,0 is a valid position, just not to be returned
        cp = [x,y,0]
        positions.append(cp)
        steps = 0
        for command in commands:
            direction = command[0]
            number = int(command[1:])
            counter = 0

            while (counter < number):
                if (direction == "U"):
                    y += 1
                elif (direction =="D"):
                    y -= 1
                elif (direction == "R"):
                    x += 1
                else:
                    x -= 1
                counter +=1
                steps += 1
                cp = [x,y,steps]
                positions.append(cp)
        both.append(positions)
    checker(both)

def checker(both):
    hits =[]
    for p1 in both[0]:
        for p2 in both[1]:
            if (p1[0] == p2[0] and p1[1] == p2[1]):
                hits.append([p1,p2])
    distances=[]
    for h in hits:
        print (h)
        dist = h[0][2] + h[1][2]
        #dist = abs(h[0]) +abs(h[1])
        distances.append(dist)
    print(hits)
    distances.sort()
    print(distances[1])


proj()

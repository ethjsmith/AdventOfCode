import math

def filehandler (f):
    instructions = []
    for line in f:
        # ok
        l = line.split(")")
        #print(line)
        l[1] = l[1][:-1]
        instructions.append([l[0],l[1]])
    return instructions

def main(ins):
    sorted = []
    for x in ins:
        flag = True
        path = []
        path.append([x[0],x[1]])
        while(flag):
            n = findnext(x[0],ins)
            if n == -1:
                sorted.append(path)
                break
            else:
                path.append(n)
                x = n
    #print(sorted)
    y=[]
    san=[]
    for x in sorted:

        #print(x[0][1])
        if x[0][1] == 'YOU':
            print('found YOU')
            y = x
        if x[0][1] == 'SAN':
            print('found SAN')
            san = x
    commonNode(y,san)
    # This is the solution to part 1:
    distances(sorted)
#278 too high
# it was 277 all along, I just typed it wrong the first time I guess :/
def commonNode(you,san):
    dist = 0
    for x in you:
        c = 0
        dist +=1
        for y in san:
            if x[0] == y[0]:
                dist += c
                dist -=1
                print("jumps required:" + str(dist))
                return dist
            c +=1
    print(-1)
    return -1


def distances(sor):
    total =0
    for x in sor:
        total += len(x)
    print ("Distance:" + str(total))
    return total

def findnext(x,ins):
    for z in ins:
        if z[1] == x:
            return [z[0],z[1]]
    return -1

print(main(filehandler(open('input.txt','r'))))

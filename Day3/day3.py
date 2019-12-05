import math
def proj():
    f = open('testfile.txt', 'r')
    both =[]
    for line in f:
        commands = line.split(",")
        positions =[]
        x=0
        y=0
        #0,0 is a valid position, just not to be returned
        cp = [x,y]
        positions.append(cp)
        for command in commands:
            direction = command[0]
            number = int(command[1:])
            #print('{0}, {1}'.format(direction,number))
            if (direction == "U"):
                y += number
            elif (direction =="D"):
                y -= number
            elif (direction == "R"):
                x += number
            else:
                x -= number
            cp = [x,y]
            positions.append(cp)
        both.append(positions)
    checker(both[0],both[1])

checker(lines1,lines2):
for p1,p2 in zip(lines1[0::2],lines1[1::2]):
    for lp1,lp2 in zip(lines2[0::2],lines2[1::2]):


lines_cross(l1,l2):
    if (l2[0][0]  < l1[0][0] < l2[1][0]):

# def proj2():
#     positions =[]
#     f = open('testfile.txt','r')
#     line1 = f.readline()
#     commands = line1.split(",")
#     x=0
#     y=0
#     for command in commands:
#         direction = command[0]
#         number = int(command[1:])
#         if (direction == "U"):
#             y += number
#         elif (direction =="D"):
#             y -= number
#         elif (direction == "R"):
#             x += number
#         else:
#             x -= number
#         cp = [x,y]
#         positions.append(cp)
#
#     line2 = f.readline()
#     commands = line2.split(",")
#     x=0
#     y=0


proj2()

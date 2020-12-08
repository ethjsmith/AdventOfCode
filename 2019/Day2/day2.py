import copy
# my performance on this day was pretty trash tbh :~0
def filehandler(f):
    #f = open('input2.txt', 'r')
    for line in f:
        x = line.split(",")
        r = []
        for z in x:
            z= int(z)
            r.append(z)
    return r

def intcode(r):
    pos = 0
    while (True):
        if r[pos] == 1:
            r[r[pos+3]] = r[r[pos+1]] + r[r[pos+2]]
        elif r[pos] == 2:
            r[r[pos+3]] = r[r[pos+1]] * r[r[pos+2]]
        elif r[pos] == 99:
            return r
        else:
            print("ERROR")
        pos +=4
    return r

# def controller(f,pos):
def umm():
    f = open('input2.txt', 'r')
    x=0
    xx=0
    for line in f:
        print('remaking file')
        l = line.split(",")
        rNEW = []
        print('converting to int')
        for zed in l:
            zed = int(zed)
            rNEW.append(zed)

    while(True):
        r = copy.deepcopy(rNEW)
        print('starting')
        r[1] = x
        r[2] = xx
        print(str(r[0]) + str(r[1]) + str(r[2]))
        print("trying with {0},{1}".format(x,xx))
        z = intcode(r)
        print("here")
        #z = intcode(f)
        if (z[0] == 19690720):
            print("that's it")
            break
        else:
            if (x < 99):
                x+=1
            else:
                x=0
                xx+=1
        print("end")

print(intcode(filehandler(open('input2.txt', "r"))))
umm()

#part2

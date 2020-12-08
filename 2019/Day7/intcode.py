# day 7, aka day 5 plus some more stuff :o

import copy
# reads the input from the file
def filehandler(f):
    for line in f:
        x = line.split(",")
        r=[]
        for z in x:
            z = int(z)
            r.append(z)
    return r

def opcode(r,params):
    p=0
    while (True):
        #print("opcode:" +str(r[p]))
        #print(r)
        if r[p] % 100 == 1:
            add(r,p)
            p+=4
        elif r[p] % 100 == 2:
            mult(r,p)
            p+=4
        elif r[p] % 100 == 3:
            inp(r,p,params)
            p+=2
        elif r[p] % 100 == 4:
            return outp(r,p)
            p+=2
        elif r[p] % 100 == 5:
            p = jumptrue(r,p)
        elif r[p] % 100 == 6:
            p = jumpfalse(r,p)
        elif r[p] % 100 == 7:
            less(r,p)
            p+=4
        elif r[p] % 100 == 8:
            equal(r,p)
            p+=4
        elif r[p] % 100 == 99:
            print("end")
            break
        else:
            print("error, code:" + str(r[p]))
            print("next :" + str(r[p+1]))
            break

def add(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]

    r[r[p+3]] = p1 + p2


def mult(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]

    r[r[p+3]] = p1 * p2
# :)
def inp(r,p,params):
    if params != None:
        r[r[p+1]] = params.pop(0)
    else:
        r[r[p+1]] = int(input("Enter INPUT:"))
def outp(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    print("out:" + str(p1))
    return p1

def jumptrue(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]
    if p1 != 0:
        return int(p2)
    else:
        return p+3
def jumpfalse(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]
    if p1 == 0:
        return int(p2)
    else:
        return p+3
def less(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]
    if p1 < p2:
        r[r[p+3]] = 1
    else:
        r[r[p+3]] = 0
def equal(r,p):
    if (r[p] //100) % 10 == 0:
        p1 = r[r[p+1]]
    else:
        p1 = r[p+1]
    if (r[p] //1000) % 10 == 0:
        p2 = r[r[p+2]]
    else:
        p2 = r[p+2]
    if p1 == p2:
        r[r[p+3]] = 1
    else:
        r[r[p+3]] = 0

def main(fl, params=None):
    return opcode(filehandler(open(fl,'r')),params)
#main('test.txt')
##opcode(filehandler(open("testfile.txt",'r')))
##opcode(filehandler(open("test2.txt",'r')))

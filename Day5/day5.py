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
            # adds 2 numbers
            r[r[pos+3]] = r[r[pos+1]] + r[r[pos+2]]
            pos +=4
        elif r[pos] == 2:
            # multiplies 2 numbers
            r[r[pos+3]] = r[r[pos+1]] * r[r[pos+2]]
            pos +=4
        elif r[pos] == 99:
            return r
        elif r[pos] == 3:
            # takes an input value and stores it at r+1
            r[r[pos+1]] = 0#input IDK what this should be
            pos +=2
        elif r[pos] == 4:
            #outputs the element ?
            print(r[r[pos+1]])
            pos += 2

        else:
            print("ERROR")

    return r
# for now, none of this works :(
def instruction(opcode,r,p1=None,p2=None,p3=None):
    print (str(opcode) + "=opcode")
    code = str(opcode)[-2:]
    code = int(code)
    if code < 10:
        modes = str(opcode)[:-1]
    else:
        modes = str(opcode)[:-2]
    modes = "0000" + modes
    if code == 1:
        #r[r[pos+3]] = r[r[pos+1]] + r[r[pos+2]]
        r[ms(modes[-3:-2],p3,r)] = r[ms(modes[-1:],p1,r)] + r[ms(modes[-2:-1],p2,r)]
    elif code == 2:
        r[ms(modes[-3:-2],p3,r)] = r[ms(modes[-1:],p1,r)] * r[ms(modes[-2:-1],p2,r)]
    elif code == 3:
        if modes == '0000':
            r[p1] = 1
        else:
            r[ms(modes,p1,r)] = 1
    elif code == 4:
        print(r[ms(modes,p1,r)])
    elif code == 99:
        print("hit code 99, escaping!")
        #break
    else:
        print("ERROR, RCODE:" + code)
        #break
# short for mode select, but I didnt wanna type that a bunch :)
def ms(mode,parameter,r):
    print("got mode:" + str(mode) + ", and Parameter:" + str(parameter))
    if mode == '0' or mode == '' or mode == '0000':
        print("returning: " +str(r[parameter]))
        return r[parameter]
    elif mode == '1':


        print("returning: " +str(parameter))
        return parameter
    else:
        print("PARAM ERROR :" + mode)
        #break

def intcode2(r):
    pos =0
    while (True):
        code = str(r[pos])[-2:]
        code = int(code)
        if code < 10:
            x = str(r[pos])[:-1]
        else:
            x = str(r[pos])[:-2]
        print(str(r[pos]) + ", Mode: "+str(x))
        if (x[-1:] == '0' or x == ''):
            #x = x[:-1]
            if r[pos] == 1:
                # adds 2 numbers
                r[r[pos+3]] = r[r[pos+1]] + r[r[pos+2]]
                pos +=4
            elif r[pos] == 2:
                # multiplies 2 numbers
                r[r[pos+3]] = r[r[pos+1]] * r[r[pos+2]]
                pos +=4
            elif r[pos] == 99:
                return r
            elif r[pos] == 3:
                # takes an input value and stores it at r+1
                r[r[pos+1]] = 1#input this is staticly set to 1 the first time :/
                pos +=2
            elif r[pos] == 4:
                #outputs the element ?
                print(r[r[pos+1]])
                pos += 2

            else:
                print("(Mode 0) ERROR, RCODE:" + str(r[pos]))
                break
        else:
            if r[pos] == 1:
                # adds 2 numbers
                r[pos+3] = r[pos+1] + r[pos+2]
                pos +=4
            elif r[pos] == 2:
                # multiplies 2 numbers
                r[pos+3] = r[pos+1] * r[pos+2]
                pos +=4
            elif r[pos] == 99:
                return r
            elif r[pos] == 3:
                # takes an input value and stores it at r+1
                r[pos+1] = 0#input IDK what this should be
                pos +=2
            elif r[pos] == 4:
                #outputs the element ?
                print(r[pos+1])
                pos += 2

            else:
                print("(mode 1) ERROR, RCODE : " + str(r[pos]))
                break
        x = x[:-1]

def intcode3(r):
    pos = 0
    while (True):
        z = int(str(r[pos])[-2:])
        print(z)
        if z == 1 or z == 2:
            instruction(r[pos],r,r[pos+1],r[pos+2],r[pos+3])
            pos +=4
        elif z == 3 or z == 4:
            instruction(r[pos],r,r[pos+1])
            pos +=2
        elif z == 99:
            print("99, Breaking!")
            break
        else:
            print("Error, code:" + str(r[pos]))
            break

# def p(x, r,pos):
#     print(x)
#     if int(x[-1:]) == 0 or x == None:
#         x = x[:-1]
#         print(r[pos])
#         return r[pos]
#     elif int(x[-1:]) == 1:
#         x = x[:-1]
#         print(pos)
#         return pos

# def intcode3(r):
#     pos =0
#     while (True):
#         # this method should be a crime
#         code = str(r[pos])[-2:]
#         code = int(code)
#         if code < 10:
#             x = str(r[pos])[:1]
#         else:
#             x = str(r[pos])[:2]
#
#
#
#         if code == 1:
#             r[p(x,r,pos)] = r[p(x,r,pos+1)] + r[p(x,r,pos+2)]
#             pos+=4
#         elif code == 2:
#             r[p(x,r,pos)] = r[p(x,r,pos+1)] * r[p(x,r,pos+2)]
#             pos+=4
#         elif code == 3:
#             r[p(x,r,pos+1)] = 0
#             pos+=2
#         elif code == 4:
#             print(r[p(x,r,pos+1)])
#             pos+=2
#         elif code == 99:
#             return r
#         else:
#             print("ERROR")
#             break
# positional argument parser... named P for ease of typing
# I think i want this to return either x or r[x] idk how that would work tho

# def controller(f,pos):
# def umm():
#     f = open('input.txt', 'r')
#     x=0
#     xx=0
#     for line in f:
#         print('remaking file')
#         l = line.split(",")
#         rNEW = []
#         print('converting to int')
#         for zed in l:
#             zed = int(zed)
#             rNEW.append(zed)
#
#     while(True):
#         r = copy.deepcopy(rNEW)
#         print('starting')
#         r[1] = x
#         r[2] = xx
#         print(str(r[0]) + str(r[1]) + str(r[2]))
#         print("trying with {0},{1}".format(x,xx))
#         z = intcode2(r)
#         print("here")
#         #z = intcode(f)
#         if (z[0] == 19690720):
#             print("that's it")
#             break
#         else:
#             if (x < 99):
#                 x+=1
#             else:
#                 x=0
#                 xx+=1
#         print("end")

print(intcode3(filehandler(open('input.txt', "r"))))
#umm()

#part2

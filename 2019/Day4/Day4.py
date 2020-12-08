# TODAY'S CHALLENGE: part 1: 5 minutes
#                    part 2: 2 hours  :(
def help():
    startingnum = 156218
    total = 0
    while (startingnum <= 652527):
        total += isvalid(str(startingnum))
        startingnum += 1
    print(total)

def isvalid(num):
    decreases = False
    adj = 0
    prev = -1
    for char in str(num):
        # this part is solid
        if int(char) < int(prev):
            decreases = True
        prev = char

    for x in range(len(str(num))):
        #print(num[x])
        if num[x] == num[x-1]:
            if num[x] != num[x-2]:
                if (x+1 < len(str(num))):
                    if num[x] != num[x+1]:
                        adj+= 1
                else:
                    adj+=1

    if not decreases:
        if adj > 0:
        #    print ("" + num + ": is valid")
            return 1
        else:
        #    print ("" + num + ": is NOT valid")
            return 0
    return 0

help()
#print(isvalid('111111'))

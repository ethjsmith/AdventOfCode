def help():
    startingnum = 156218
    total = 0
    while (startingnum <= 652527):
        total += isvalid(startingnum)
        startingnum += 1
    print(total)

def isvalid(num):
    adjacent = 0
    decreases = False
    prev = -1
    prev2 = -1
    for char in str(num):
        # this part is solid
        if int(char) < int(prev):
            decreases = True
            break

        if int(char) == int(prev):
            adjacent += 1

        if (adjacent > 0) and int(prev2) == int(char):
            adjacent -= 1
        if prev != -1:
            prev2 = prev
        prev = char


    if (adjacent > 0) and not decreases:
        return 1
    return 0


help()

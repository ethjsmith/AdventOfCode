import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst
# input looks like this
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0

# mask starts at char7?
# mem target is harder ( could be multidigit, but starts at char5 )
# mem number got with split on " = "?

def formatList():
    formatted = []
    lst = getInput()
    tmp = ""
    for x in lst:

        print(x)
        s = x.split(" = ")
        if s[0] == "mask":
            if tmp != "":
                formatted.append(tmp)
            tmp = [s[1]]
        else:
            tmp.append((s[0][4:-1],s[1]))
    else:
        formatted.append(tmp)
    return formatted

def getNumber():
    lst = formatList()
    mem = {}
    for set in lst:
        msk = set[0]    # unpack the mask
        for instruction in set[-1:]:        # loop though the other instructions, writing to file?
            result = ""
            # instruction [0] is where to save
            # instruction [1] is a binary number to be "combined" with the mask for the writable number
            b = format(int(instruction[1]),'#036b')
            for x,char in enumerate(b): # does this work ?
                if msk[x] == "X":
                    result += char
                else:
                    result += msk[x]
            mem[instruction[0]] = result
    return mem


def getAnswer():
    a = getNumber()
    # add up the stuff
#print(formatList())
print(getNumber())

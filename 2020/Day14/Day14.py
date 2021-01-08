import sys, math
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

        #print(x)
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
        for instruction in set[1:]:        # loop though the other instructions, writing to file?
            result = ""
            # instruction [0] is where to save
            # instruction [1] is a binary number to be "combined" with the mask for the writable number
            b = format(int(instruction[1]),'036b')
            for x,char in enumerate(b): # does this work ?
                if msk[x] == "X":
                    result += char
                else:
                    result += msk[x]
            mem[instruction[0]] = result
    return mem



def getAddress():
    lst = formatList()
    mem = {}
    for set in lst:
        msk = set[0]
        for instruction in set[1:]:
            result = ""
            len = 0
            # now we're working with the address instead of the number to write
            b = format(int(instruction[0]), '036b')
            #print(f"{b} is our base target ( in binary{instruction[0]})")
            for x,char in enumerate(b):
                if msk[x] == "X":
                    result += "X" # do this after
                    len += 1 # umm
                elif msk[x] == "0":
                    result += char
                else:
                    result += msk[x]
            #print(f"creating permutations of {result},{len}")
            all = createPermutations(result,len)
            for x in all:
                #print(f'added {instruction[1]} to mem at {int(x,2)}')
                mem[int(x,2)] = instruction[1]
    return mem
    #return all

def createPermutations(base,leng):
    blist = []
    bin_arr = range(0, int(math.pow(2,leng)))
    bin_arr = [bin(i)[2:] for i in bin_arr]
    max_len = len(max(bin_arr, key=len))
    bin_arr = [i.zfill(max_len) for i in bin_arr]
    for x in bin_arr:
        entry = ""
        tmp = x
        for cha in base:
            if cha == "X":
                entry += tmp[0]
                tmp = tmp[1:] # maybe?
            else:
                entry += cha
        blist.append(entry)
    return blist

def getAnswer():
    dic = getNumber()
    total = 0
    for key in dic:
        total += int(dic[key],2)
    return total

def get2Answer(): # it would be better to rework getAnswer(), but I don't want to deal with the slightly different output formats 
    dic = getAddress()
    total = 0
    for k in dic:
        total += int(dic[k]) # heh
    return total
print(getAnswer()) # Part 1
#print(createPermutations("1X3X82XXXXXXXXXXXXXXXX4",16)) # testing
#print(createPermutations('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',34)) # this one might eventually work, VERY large tho
#print(createPermutations('X1001X',2))
print(get2Answer())

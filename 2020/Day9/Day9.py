import sys, re

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    lst = [int(x) for x in lst]
    return lst


# finds a number which adds
def findAdd(p, ind, lst): # p = how many previous the nunber looks at
    #print(f"finding {lst[ind]}")
    for x in lst[ind-p:ind]:
        compliment = lst[ind] - x
        for xx in lst[ind-p:ind]:
            if xx == compliment and xx != lst[ind]:
                #print(f"Found a match with {xx} + {lst[ind]}")
                return True
    return False

# uses find add
def doIt(p,i):
    lst = getInput()
    x = True
    while x == True:
        x = findAdd(p,i,lst)
        i += 1
    return lst[i-1]

def findContiguousList(p,i):
# this is sooo bad, it really should remove the last element, and add the next, but instead it recalculates the entire list
# In practice that means that it takes awhile to get through this
    lst = getInput()
    target = doIt(p,i)
    num = 3 # number of elements to add, don't have to worry about two, as we already tried that ...
    while True:
        for i, ind in enumerate(lst):
            ret = []
            if i + num < len(lst):
                result = 0
                x = 0
                while x < num:
                    #print (f"adding {lst[i+ x]}")
                    ret.append(lst[i+x])
                    result += lst[i+x]
                    x+= 1
                #print(f"result:{result}" )
                if result == target:
                    return True,ret
        num +=1
        if num > len(lst):
            return False

def getMaxMin(a,b):
    lst = findContiguousList(a,b) # change these for the main problem
    return max(lst[1]) + min(lst[1])

#print(findContiguousList(5,5)[1])

print(doIt(25,25)) # part 1
print(getMaxMin(25,25)) # part 2

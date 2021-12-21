import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def format():
    l = getInput()
    tr = []
    for line in l:
        tr.append([int(a) for a in str(line)])
    return tr

# this one is gonna be... interesting
#print(format())

def simul8():
    l = format()

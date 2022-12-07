# I wrote a lil script (util.py) that downloads automatically the input, I think just writing it to the file and then reading from is good for now, later I could make that better 
def getInput(y ,path="2022/Day4/"):
    with open(f"{path}{y}.txt") as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    newlist= []
    for line in lst:
        parts = line.split(",")
        tup = []
        for part in parts:
            z = part.split("-")
            tup.append((int(z[0]),  int(z[1])))
        newlist.append(tup)
    return newlist
    # this is some gross data to look at 
    # I'm sure it will only get worse... :^)


# check if a pair fully contains another 

def check_all_overlap(a,b):
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    if b[0] >= a[0] and b[1] <= a[1]:
        return True
    return False

#part 2 code  

def lap(a,b):
    if a[0] >= b[0] and a[0] <= b[1]:
        return True
    if a[1] >= b[0] and a[1] <= b[1]:
        return True
    return False

def together():
    inp = getInput("input")
    total = 0
    any_overlap = 0
    for x in inp:
        if check_all_overlap(x[0],x[1]):
            total += 1
        if lap(x[0],x[1]) or lap(x[1],x[0]): # do it in both directions
            any_overlap += 1
    return total, any_overlap # part 1, part 2 

# 535 too low 


print(together())

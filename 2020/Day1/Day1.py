
def getInput(fname):
    with open(fname) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def entries_sum_to_2020(lst):
    for x in lst:
        for y in lst:
            total = x + y
            if int(x) + int(y) == 2020:
                return int(x)*int(y)
    return -1

def entries_sum_to_2020_2(lst):
# a good programmer might just modify the first function to take a variable or something...
# or they might write a function that wasn't On^2 and then On^3
    for x in lst:
        for y in lst:
            for z in lst:
                if (int(x) + int(y) + int(z) == 2020):
                    return int(x)*int(y)*int(z)
    return -1

#print(entries_sum_to_2020(getInput("input.txt")))
print(entries_sum_to_2020_2(getInput("input.txt")))

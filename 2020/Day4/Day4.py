import re
def getInput(fname):
    with open(fname) as f:
        lst = f.readlines()
    #lst = [x.strip() for x in lst] # in this case we want all those weird characters
    return lst

def formatInput(lst):
    # looks like a great case for a dictionary, althought I don't actually
    # have much experience with dicts, but it seems like I can each "passport" into a dict
    # and then check for each field or something
    ret = []
    component = ""
    for x in lst:
        if x == "\n":
            component = component.replace("\n", " ")
            ret.append(component[:-1]) # this is kinda dumb probably, but it trims the tailing space
            component = ""
        else:
            component += x
    component = component.replace("\n", " ")
    ret.append(component[:-1])
    # ret is now a list of complete single line passports
    return ret

def checkPassports(lst):
    valid_count=0
    for passport in lst:
    #    print(passport)
        pport = {}
        p = passport.split(" ")
        #print(p)
        for field in p:
            f = field.split(":")
            pport[f[0]] = f[1]
        #print (pport)
        if "byr" in pport and "iyr" in pport and "eyr" in pport and "hgt" in pport and "hcl" in pport and "ecl" in pport and "pid" in pport:
            valid_count += 1# I dunno about this line lol
        # for part 2 we call validate instead of checking like this
    return valid_count

def validate(d):
    # if any tests fails, return 0, else return 1
    if d['byr'] < 1920 or d['byr'] > 2002:
        return 0
    if d['iyr'] < 2010 or d['iyr'] > 2020:
        return 0
    if d['eyr'] < 2020 or d['eyr'] > 2030:
        return 0
    if d['hgt'][-2:]

    if d['hcl'] re.search(\#\w\w\w\w\w\w) # something like this

    if d['ecl'] not in ['amb',"blu","brn","gry","grn","hzl","oth"]:
        return 0
    if d['pid'] # just a 9 digit number 


#print(getInput("example.txt"))
# print(formatInput(getInput("example.txt")))
print(checkPassports(formatInput(getInput("input.txt"))))

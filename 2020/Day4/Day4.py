# this one was hard because I made a dumb mistake ( in the PID regex allowing for 10 characters worth of letters), and it took awhile to find
# leaving all the comments that I used to debug :^)

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
            #valid_count += 1# I dunno about this line lol
            valid_count += validate(pport)
        # else:
        #     print(pport)
        #     print("failed by not having enough fields")
        # for part 2 we call validate instead of checking like this
    return valid_count

def validate(d):
    #print(" ")
    print(d['pid'])
    v = 0 # using this way to #print all errors in a line
    # if any tests fails, return 0, else return 1
    if int(d['byr']) < 1920 or int(d['byr']) > 2002:
        #print(d['byr'] +" failed on BYR")
        v -= 1
    if int(d['iyr']) < 2010 or int(d['iyr']) > 2020:
        #print(d['iyr'] +" failed on iyr")
        v -= 1
    if int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
        #print(d['eyr'] + " failed on eyr")
        v -= 1
    if d['hgt'][-2:] == "in":
        if int(d['hgt'][:-2]) < 59 or int(d['hgt'][:-2]) > 76:
            #print(d['hgt'] +" failed on HGT_IN_bounds")
            v -= 1
    elif d['hgt'][-2:] == "cm":
        if int(d['hgt'][:-2]) < 150 or int(d['hgt'][:-2]) > 193:
            #print(d['hgt'] +" failed on HGT_CM_bounds")
            v -= 1
    else:
        #print(d['hgt'] +" failed on HGT_units")
        v -= 1 # this should catch a fully invalid height, not everything
    if  not re.search("#[0-9a-f]{6}",d['hcl']): # something like this
        #print(d['hcl'] + " failed on HCL")
        v -= 1
    if d['ecl'] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
        #print(d['ecl'] +" failed on ECL")
        v -= 1
    if not re.search("^[0-9]{9}$",d['pid']): # just a 9 digit number
        print(d['pid'] +" failed on PID")
        v -= 1
    if v == 0:
        #print("Valid pport")
        return 1
    #print(str(v) + "errors")
    return 0

# its not 148
#print(getInput("example.txt"))
# print(formatInput(getInput("example.txt")))
print(checkPassports(formatInput(getInput("input.txt"))))

def getInput(fname): # TODO: put this in it's own class so I can just import it or something, I expect Ill be using it a lot
    with open(fname) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def count_valid_passwords(lst):
    count = 0 # running counter
    for passw in lst:
        components = passw.split(":") # break up the string into the components
        limits = components[0].replace(' ','-').split('-') # this is kind of dumb
        lwr = int(limits[0])
        upr = int(limits[1])
        char = limits[2]
        lim = 0
        #print(f"lower: {lwr}, upper: {upr}, Character:{char}, password:{components[1]}") # debug line
        for x in components[1]:
            if x == char:
                lim += 1
        if lim >= lwr and lim <= upr:
            count += 1
    return count

def count_valid_passwords_mk2(lst):
    count = 0 # running counter
    for passw in lst:
        components = passw.split(":") # break up the string into the components
        limits = components[0].replace(' ','-').split('-') # this is kind of dumb
        lwr = int(limits[0])
        upr = int(limits[1])
        char = limits[2]
        lim = 0 # I like copying code as much as the next CS student, but it might be better if this was it's own function

        if components[1][lwr] == char:
            lim += 1
        if components[1][upr] == char:
            lim += 1
        if lim == 1:
            count += 1
    return count

#print(count_valid_passwords(getInput("input.txt")))
print(count_valid_passwords_mk2(getInput("input.txt")))

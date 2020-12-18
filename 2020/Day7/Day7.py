import sys, re
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    lst = [x.strip(".") for x in lst]
    return lst

# could use recursion here ?

def formatBags(): # explaining the whole process because this is confusing, and maybe bad
    formatted = []
    lst = getInput()
    for rule in lst:
        component = rule.split(" contain") # split the rule into its components, the rule, and the action
        action = component[1].split(",") # split the action into pieces for multipart actions
        tmp = []
        for i, ac in enumerate(action):
        #for ac in action:
            #print(ac)
            tmp = ac
            #if ac != " no other bags": # commenting this to keep the numbers, which are now needed
            #    tmp = ac[3:]
            if ac[-3:] == "bag":
                tmp = tmp + "s"
            action[i] = tmp
        formatted.append([component[0],action]) # add the formatted parts to a returnable lst
    return formatted
    #return would look like [['Condition'], [[action,number],[action2, number]]]]
def makeRuleDict(): # turns this into a dictionary of rules and their links
    formatted = formatBags() #
    rules = {}
    for rule in formatted:
        rules[rule[0]] = rule[1]
    #for k, v in rules.items():
        #print(k + ":" + str(v))
    return rules

#print(makeRuleDict()) # testing


def holdsgold (di, ind):
    counter = 0
    #for result in t[1]:
    for result in di[ind]:
        print(result)
        if re.search("shiny gold bags",result[3:]):
            counter += 1
        elif re.search(" no other bags", result):
            counter += 0 # lol this is useless
        else:
            counter += holdsgold(di,result[3:])
    if counter > 1:
        counter = 1
    return counter
#print(formatBags())


def canHoldt(): # t can be our gold bag perhaps
    #rules = formatBags()#
    rules = makeRuleDict()
    ways = 0
    for rule in rules:
    #for i, rule in enumerate(rules):
        print("######" + rule + "######")
        ways += holdsgold(rules,rule)
        #print(yeah)
    return ways
# so how do I actually solve this?
# the question is, how many outerlevel bags can eventually hold a shiny gold bag?

def howManyInside(di,ind):
    count = 0
    for result in di[ind]:
        print(result)
        if re.search(" no other bags", result):
            count += 0 # for the bag containing no other bags
        else:
            loopnum = int(result[1])
            while loopnum > 0:
                loopnum -= 1
                count += 1 + howManyInside(di,result[3:])
    return count

print(howManyInside(makeRuleDict(),"shiny gold bags")) # parts 2 ?
#print(canHoldt())

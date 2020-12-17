import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
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
            if ac != " no other bags":
                action[i] = ac[3:]

            if ac[-3:] == "bag": ############################## HERE 
                action[i] = ac + "s"
        action[len(action)-1] = action[len(action)-1][:-1] # removes trailing period at the end of rules

        # This part doesn't work right rn
        # action_parts = []
        # for entry in action: # split each portion of an action into the name, and the quantity
        #     action_parts.append([entry[2:],entry[:3]]) # this is getting... messy
        formatted.append([component[0],action]) # add the formatted parts to a returnable lst
        # action_parts = []
    return formatted
    #return would look like [['Condition'], [[action,number],[action2, number]]]]
def makeRuleDict(): # turns this into a dictionary of rules and their links
    formatted = formatBags() #
    rules = {}
    for rule in formatted:
        rules[rule[0]] = rule[1]
    return rules

print(makeRuleDict())
def canHoldt(t): # t can be our gold bag perhaps
    rules = formatBags()
    ways = 0
    for rule in rules:
        print(yeah)
# so how do I actually solve this?
# the question is, how many outerlevel bags can eventually hold a shiny gold bag?

def holdsgold (di, ind):
    counter = 0
    #for result in t[1]:
    for result in di[ind]:
        if re.search("shiny gold bag",result):
            counter += 1
        elif re.search("no other bags", result):
            counter += 0 # lol this is useless
        else:
            counter += holdsgold(di,result)
    return counter
#print(formatBags())

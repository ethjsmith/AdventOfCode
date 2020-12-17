import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def splitIntoGroups(): # splits the list lines into respective groups
    groups = []
    lst = getInput()
    entry = ""
    for line in lst:
        entry = entry + line
        if line == "":
            entry.replace(" ", "") # strip any spaces
            groups.append(entry)
            entry = ""
    entry.replace(" ", "") # get the last one in the list...
    groups.append(entry)
    return groups

def uniqueCount():# returns the number of questions answered by each group
    sum = 0
    groups = splitIntoGroups()
    #print(groups)
    for g in groups:
        unique = "".join(set(g))
        answers = len(unique)
        #print(answers)
        sum += answers
    return sum

def groupPeople():
    allgroups = []
    onegroup = []
    lst = getInput()

    for person in lst:
        if person == "":
            allgroups.append(onegroup)
            onegroup = []
        else:
            onegroup.append(person)
    allgroups.append(onegroup)
    return allgroups

def majorityCount(): # this is a bad function name because it isn't really acurate
    groups = groupPeople()
    total = 0

    for group in groups:
        grouptotal = 0
        keys = {}
        for person in group:
            for letter in person:
                if letter not in keys:
                    keys[letter] = 1
                else:
                    keys[letter] = keys[letter] +1
        #print(keys)
        for key in keys:
            if keys[key] == len(group):
                grouptotal += 1
        #print (grouptotal)
        total = total + grouptotal
    return total

print(uniqueCount())# answer to part 1

# part 2 breaks how I was handling the problem, I have to keep track of the data separately now
print(majorityCount()) # answer to part 2

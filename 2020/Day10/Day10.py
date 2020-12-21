import sys
def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    lst = [int(x) for x in lst]
    lst.sort()
    # don't forget to add device power rating
    # best practice might be also adding the zero ?
    lst.append(lst[len(lst)-1]+3)
    #print(lst)
    return lst

def differences(): # part 1 easier than I was expecting...
    lst = getInput()
    jolts = {1:0,2:0,3:0}
    current =0
    for adapter in lst:
        jolts[adapter-current] = jolts[adapter-current] + 1
        current = adapter
    return jolts

def multipyAnswers(): # answer for part 1
    jolts = differences()
    return jolts[1] * jolts[3]


# had to do some research on this topic, and found this ...
# each item can't be reached, except the first, which can,
# now loop through the list and check every item for
def answer():
    lst = getInput()
    paths = {0:1}
    for x in lst:
        paths[x] = 0
    lst.insert(0,0)
    for i,num  in enumerate(lst):
        for x in range(1,3):
            if i+x < len(lst)-1 and lst[i+x]-num <= 3:
                print(f"can get from {num} to {lst[i+x]}, +1 route ")
                paths[lst[i+x]] += paths[lst[i]]



        # x = 1
        # while i+x < len(lst)-1:
        #     if lst[i] - lst[i+x] <3:
        #         paths[lst[i+x]] +=paths[lst[i]]
        #         x+= 1

    total = 0
    print(paths)
    for x in paths:
        total += x
    return paths[lst[len(lst)-1]]

print(answer())


# def differentCombinations():
#     combos = 1 # starts at one, for the one we already know ( the sorted list )
#     lst = getInput()
#     current = 0
#     # actually it should remove the unnessesary element, and restart or something ?
#     for i, adapter in enumerate(lst):
#         if adapter - current < 3:
#             for z in range(1,3):
#                 if lst[i+z] - current <=3:
#                     combos += 1
#         current = adapter
#     return combos
#
# def findPermutation(lst,current):
#     for i, adapter in enumerate(lst):
#         if adapter - current < 3:
#             for z in range(1,3):
#                 if i+z < len(lst):
#                     if lst[i+z] - current <=3:
#                         print(f"removing {lst[i]}")
#                         print(lst[i+z:])
#                         return 1 + findPermutation(lst[i+z:],current)
#         current = adapter
#     return 1
#
# def loopList(lst):
#     print(lst)
#     count =1
#     for i, a in enumerate(lst):
#         if i+1 < len(lst):
#             if lst[i+1] - lst[i] <3:
#                 count *= findPermutation(lst[i:],0)
#
#     return count
# #print(multipyAnswers())
#
# #print(differentCombinations())
# #print(findPermutation(getInput(),0))
# print(loopList(getInput()))

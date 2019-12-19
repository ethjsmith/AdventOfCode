from intcode import main
import os, itertools
#main("test.txt")
#print(os.system("intcode.py <1\\n1"))
#x = main('test.txt',[1,1])



def checkPermutation(perm,file):
    # this is the dumbest thing I've EVER made
    # I feel like I say that at least once a day working on this stuff
    return main('input.txt',[perm[4],main(file,[perm[3],main(file,[perm[2],main(file,[perm[1],main(file,[perm[0],0])])])])])
    #return main('test.txt',[perm[0],0])

def permset(pm):
    maxes = []
    permz = itertools.permutations(pm)
    for x in permz:
        maxes.append(checkPermutation(x,'input.txt'))
    print(max(maxes))

# wrong : 51732
#         11828
permset([0,1,2,3,4])

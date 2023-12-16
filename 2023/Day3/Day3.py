import sys

def getInput(file):
    with open(file) as f:
        lines = [l.strip() for l in f]
    return lines

all_indices = {}
file = getInput("2023/Day3/input.txt")
# generate grid of falses
for line in range(len(file)):
    for char in range(len(file[line])):
        all_indices[(line,char)] = False
def convert_to_true(x,y):
    for a in [x-1, x, x+ 1]:
        for b in [y-1, y ,y+1]:
            all_indices[(a,b)] = True
            
for line in range(len(file)):
    for char in range(len(file[line])):
        if file[line][char] not in ['1','2','3','4','5','6','7','8','9','0','.']:
            # convert all adjacent indices to be valid part numbers 
            print(f"{file[line][char]}")
            convert_to_true(line,char)



def p():
    # debug function for displaying the thing idk 
    for line in range(len(file)):
        for char in range(len(file[line])):
            a = all_indices[(line,char)]
            if a:
                print("O",end='')
            else:
                print(".",end="")
            # print(all_indices[(line,char)],end='')
        print(f"{line}")
        
p()

# now we need to do some more stuff I guess ? 

# go thru and find/assemble numbers, then check if they are valid part numbers 

def assemble_numbers():
    # gotta constantly loop bc idk LOL ??
    numbers = [] 
    prev = ''
    for line in range(len(file)):
        for char in range(len(file[line])):
            # for some reason, this function moves on to the next line before everything it is doing is finished??? 
            character = file[line][char]
            if character in ['0','1','2','3','4','5','6','7','8','9']:
                # this is a number
                prev += character 
            else:
                if prev != "":
                    numbers.append((prev,(line,char-1))) # I think I need the minus 1? idk really :/ 
                    prev = ""
        if prev != "":
            numbers.append((prev,(line,char-1))) # I think I need the minus 1? idk really :/ 
            prev = ""
            # that should get me my list... now just need to do the thing I think :) 
    print(numbers)
    return numbers
            
def check_valid_numbers(num):
    # a num looks like ["123", (4,6)] I hope :) 
    for x in range(len(num[0])):
        # print(x)
        # print(f"for {num[0]} checking ({num[1][0]},{num[1][1]-x}) which is {all_indices[(num[1][0],num[1][1-x])]}")
        if all_indices[(num[1][0],num[1][1]-x)] == True:
            return True
    return False 
    # this is a nightmare, lmfao I feel dumb ? I guess maybe if it works we'll see... 
    
n = assemble_numbers()

valid_nums = []
for x in n:
    if check_valid_numbers(x):
        valid_nums.append(int(x[0]))

print(valid_nums)
print(sum(valid_nums))
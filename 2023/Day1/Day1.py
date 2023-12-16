import re
numz = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
}
def getInput(file):
    with open(file) as f:
        lines = [l for l in f]
    return lines


def numbers(lines):
    ret = []
    for line in lines:
        for x in line:
            if x.isdigit():
                d1 = int(x)
                break
        for x in line[::-1]:
            if x.isdigit():
                d2 = int(x)
                break
        ret.append((int(str(d1) + str(d2))))
    return ret
def numbers3(lines):
    results = []
    for line in lines:
        matches = re.findall(r"\d", line)
        print(matches)
        results.append(
            10 * int(matches[0]) +  int(matches[-1])
        )
    print(results)
    return results
def add(nums):
    total = 0
    for num in nums:
        total+= num
    return total

print(f"part 1: {add(numbers3(getInput('2023/Day1/test.txt')))}")

def numbers2(lines):
    results = []
    for line in lines:
        matches = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
        reverse = re.findall(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d", line[::-1]) # This is dumb and I hate it 
        # the problem is that getting a match consumes the characters, so oneight returns only 1 for example
        # I don't know regex-fu enough to fix that, so instead a scuffed solution
        results.append(
            10 * to_num(matches[0]) + to_num(reverse[0])
        )
    return results
def to_num(n):
    try:
        return int(n)
    except:
        try: # haha this is terrible too, a nested try catch :) 
            return numz[n]
        except:
            return numz[n[::-1]]
print(f"Part 2: {add(numbers2(getInput('2023/Day1/input.txt')))}")

import sys

def getInput():
    with open(sys.argv[1]) as f:
        lst = f.readlines()
    lst = [x.strip() for x in lst]
    return lst

def findox(f,d,c):
    print(f"f:{f}, d:{d}, c:{c}")
    if len(f) == 1:
        return f
    good = []
    for num in f:
        if int(num[d]) == c:
            good.append(num)
    return good

def dfreq(f,d): # frequency of digit at d in lines
    out = {
        1:0,
        0:0
    }
    for x in f:
        if int(x[d]) == 1:
            out[1] = out[1] + 1
        else:
            out[0] = out[0] + 1
    print(f"position:{d}, result:{out}")
    if out[1] >= out[0]:
        return 1
    else:
        return 0

r = getInput()
print(f"INPUT RAW:{r}")
out = ""
ox = r
co2 = r
ntmp = 0
for x in range(len(r[0])):
    tmp = dfreq(r,x)
    out += str(tmp)
for x in range(len(ox[0])):
    tmp = dfreq(ox,x)
    ox = findox(ox,x,int(tmp))
for x in range(len(co2[0])):
    tmp = dfreq(co2,x)
    if tmp == 1:
        ntmp = 0
    else:
        ntmp = 1
    co2 = findox(co2,x,int(ntmp))

#print(out)
print(f"ox:{int(ox[0],2)}")
print(f"co2:{int(co2[0],2)}")
print(f"life support rating: {int(ox[0],2) * int(co2[0],2)}")
opposite = ""
for x in out:
    if x == "1":
        opposite += "0"
    else:
        opposite += '1'
realout = int(out,2)
realopp = int(opposite,2)
print(f"{realout},{realopp}")
print(f"power consumption: {realout * realopp}")

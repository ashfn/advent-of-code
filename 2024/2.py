nums = []

x = input()
while(x!=""):
    arr = list(map(int, x.split(" ")))
    nums.append(arr)
    x = input()


def check(arr, r=True):
    lDiff = 0
    fails = 0
    for i in range(len(arr)-1):
        dif = arr[i+1]-arr[i]
        if(lDiff>0 and dif <0):
            fails+=1
        if(lDiff<0 and dif > 0):
            fails+=1
        if(dif==0):
            fails+=1
        if not abs(dif) <= 3:
            fails+=1
        if(fails>0 and r):
            for d in range(len(arr)):
                x = arr[0:d]
                for ii in range(d+1, len(arr), 1):
                    x.append(arr[ii])
                print(f"{arr} {x}")
                if(check(x, False)):
                    return True
            return False
        elif(fails>0):
            return False
        lDiff = dif
    return True


c = 0
for arr in nums:
    if(check(arr)):
        c+=1

print(c)
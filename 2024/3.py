mem = open("input.txt", "r").read()
# mem="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

total = 0

enabled = True

for i in range(len(mem)-7):
    x = "".join(mem[i:i+4])
    a = "".join(mem[i:i+7])
    

    if(x=="do()"):
        enabled=True
    elif(a=="don\'t()"):
        enabled=False
    elif(x=="mul("):
        inside = ""
        for d in range(i+4, len(mem), 1):
            c = mem[d]
            if(c==")"):
                break
            elif(c!=")" and c!="," and not c.isdigit()):
                inside = None
                break
            else:
                inside+=c
        if(inside!=None):
            a = list(map(int, inside.split(",")))
            if(enabled):
                total+=(a[0]*a[1])
print(total)
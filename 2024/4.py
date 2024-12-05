search = list(map(list, open("input.txt", "r").read().split("\n")))

# print(search)

dirs = [
    [0, 1],
    [0, -1],
    [1, 1],
    [1, -1],
    [1, 0],
    [-1, 0],
    [-1,-1],
    [-1, 1]
]

count = 0

for y in range(len(search)):
    for x in range(len(search[y])):
        for direction in dirs:
            mx = x+(direction[0]*3)
            my = (y+direction[1]*3)
            if(mx<0 or mx>len(search[y])-1):
                continue
            if(my<0 or my>len(search)-1):
                continue
            s = ""
            for i in range(4):
                nx = x+(direction[0]*i)
                ny = y+(direction[1]*i)
                v = search[ny][nx]
                s+=v
            if(s=="XMAS"):
                count+=1
print(count)
        # print(search[y][x])
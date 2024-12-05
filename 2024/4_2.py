search = list(map(list, open("input.txt", "r").read().split("\n")))

# print(search)

dirs = [
    [1, 1],
    [1, -1],
    [-1,-1],
    [-1, 1]
]

count = 0

aCoords = []

for y in range(len(search)):
    for x in range(len(search[y])):
        for direction in dirs:
            mx = x+(direction[0]*2)
            my = (y+direction[1]*2)
            if(mx<0 or mx>len(search[y])-1):
                continue
            if(my<0 or my>len(search)-1):
                continue
            s = ""
            for i in range(3):
                nx = x+(direction[0]*i)
                ny = y+(direction[1]*i)
                v = search[ny][nx]
                s+=v
            if(s=="MAS"):
                ax = x+direction[0]
                ay = y+direction[1]
                ac = [ax, ay]
                aCoords.append(ac)
                if(aCoords.count(ac)>1):
                    count+=1


print(count)
        # print(search[y][x])
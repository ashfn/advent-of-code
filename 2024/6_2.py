x = list(map(list, open("input.txt", "r").read().split("\n")))

ostart = [0, 0, 0]


for i in range(len(x)):
    for ii in range(len(x[i])):
        if x[i][ii] == "^":
            ostart = [ii, i, 0]

dirs = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0]
]

def switchDir(curDir):
    curDir+=1
    if(curDir>3):
        curDir=0
    return curDir

loops = 0

for oy in range(len(x)):
    for ox in range(len(x[i])):
        if(ox==ostart[0] and oy == ostart[1]):
            continue
        print(f"x{ox} y{oy}")
        start = ostart

        newObstacle = []
        for _ in x:
            newObstacle.append(_.copy())
        newObstacle[oy][ox]="#"

        curloc = start

        curDir = 0

        visited = [start]


        while True:
            direction = dirs[curDir]
            newLoc = [curloc[0]+direction[0], curloc[1]+direction[1], curDir]


            if(newLoc[1]<0 or newLoc[1]>len(newObstacle)-1):
                break
            if(newLoc[0]<0 or newLoc[0]>len(newObstacle[0])-1):
                break
            atNL = newObstacle[newLoc[1]][newLoc[0]]

            if(atNL=="#"):
                # Switch direction
                curDir = switchDir(curDir)

                if(visited.count(newLoc)>1):
                    print("Found a loop!")
                    loops+=1
                    break
                visited.append(newLoc)
            else:
                curloc = newLoc
                # Add to visited
                

print(loops)
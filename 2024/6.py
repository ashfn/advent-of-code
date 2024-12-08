x = open("input.txt", "r").read().split("\n")

start = [0, 0]

for i in range(len(x)):
    for ii in range(len(x[i])):
        if x[i][ii] == "^":
            start = [ii, i]

visited = [start]

distinct = 1

curloc = start

dirs = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0]
]

curDir = 0

def switchDir():
    global curDir
    curDir+=1
    if(curDir>3):
        curDir=0

while True:
    direction = dirs[curDir]
    newLoc = [curloc[0]+direction[0], curloc[1]+direction[1]]
    print(newLoc)
    if(newLoc[1]<0 or newLoc[1]>len(x)-1):
        break
    if(newLoc[0]<0 or newLoc[0]>len(x[0])-1):
        break
    atNL = x[newLoc[1]][newLoc[0]]
    if(atNL=="#"):
        # Switch direction
        switchDir()
    else:
        if not newLoc in visited:
            distinct+=1
            visited.append(newLoc)
        curloc = newLoc

print(distinct)
        # Add to visited
        


import math

x = open("input.txt", "r").read().split('\n')

lines = []
for i in x:
    d = i.split(":")
    vals = list(map(int, d[1][1:].split(" ")))
    lines.append([int(d[0]), *vals])

# True means add, False means multiple, None is to start it off
def getResults(nums,):
    results = set()
    if len(nums) >= 2:
        addval = nums[0] + nums[1]
        mulval = nums[0] * nums[1]
        concval = (nums[0] * (10**(math.floor(math.log(nums[1], 10))+1)))+nums[1]

        if len(nums) == 2:
            results.update({addval, mulval, concval})
        else:
            results.update(getResults([addval, *nums[2:]]))
            results.update(getResults([mulval, *nums[2:]]))
            results.update(getResults([concval, *nums[2:]]))

    return results

total = 0

print(lines)

x = 0

for i in lines:
    print(x)
    goal = i[0]
    nums = list(getResults(i[1:]))
    # print(f"{goal} {nums}")
    if goal in nums:
        total+=goal
    x+=1

print(total)

# print(len(getResults([891,8,8,8,9,7,6,87,4,5,8,8])))
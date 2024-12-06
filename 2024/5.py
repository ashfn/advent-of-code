rules = open("rules.txt", "r").read().split("\n")
pages = open("pages.txt", "r").read().split("\n")

rules = list(map(lambda x: x.split("|"), rules))
pages = list(map(lambda x: x.split(","), pages))

total = 0

def check(pagel):
    for rule in rules:
        if rule[0] in pagel and rule[1] in pagel:
            a = pagel.index(rule[0])
            b = pagel.index(rule[1])
            if not a < b:
                return False
    return True



for pagel in pages:
    correct=True
    while not check(pagel):
        for rule in rules:
            print(f"{rule[0]} {rule[1]} {pagel}")
            if rule[0] in pagel and rule[1] in pagel:
                # print(pagel)
                a = pagel.index(rule[0])
                b = pagel.index(rule[1])
                if not a < b:
                    print(rule)
                    pagel[a], pagel[b] = pagel[b], pagel[a]
                    correct = False
                    print(pagel)
    if not correct:
        midI = int((len(pagel)+1)/2)-1
        print(pagel[midI])
        total+=int(pagel[midI])

print(total)
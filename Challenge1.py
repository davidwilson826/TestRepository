done = "false"
cubes = [1]
sums = [1]
currentnum = 2

while done == "false":
    cubes = cubes+currentnum**3
    sums = sums+[x+currentnum**3 for x in cubes]
    for x in sums.sort():
        if sums.count(x) > 1 and done == "false":
            print(x)
            done = "true"
    currentnum += 1

print(sums)
cubes = [1]
sums = [1,1]
cubes = cubes+8
sums = sums+[x+8 for x in cubes]

for x in sums.sort():
    if sums.count(x) > 1:
        print(x)

print(sums)
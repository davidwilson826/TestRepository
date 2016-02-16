from random import randint

size = 3 #input("Matrix size? ")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mlist = [alpha[randint(0, 25)] for x in [1]*size**2]
print(mlist)

print("Matrix Generated: ")

pos = [0, 0]

while pos[0] < size:
    toprint = mlist[pos[0]*size+pos[1]]
    if pos[1]+1 == size:
        print(toprint)
        pos[0] += 1
        pos[1] = 0
    else:
        print(toprint, end=" ")
        pos[1] += 1
        
pos = [0, 0]
nprint = 0
hdist = size
vdist = 0

while nprint < size**2-1:
    print(mlist[pos[0]*size+pos[1]], end=" ")
    if pos[1] == hdist:
        pos[0] += 1
    elif pos[0] == vdist:
        pos[1] += 1
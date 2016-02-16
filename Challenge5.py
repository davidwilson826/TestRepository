from random import randint

size = 5 #input("Matrix size? ")

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
vdist = size
direc = [1, 0]

while nprint < size**2-1:
    print(mlist[pos[0]*size+pos[1]], end=" ")
    pos = [pos[0]+direc[1], pos[1]+direc[0]]
    nprint += 1
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

hdist = size
vdist = size
pos = [0, 0]
nprint = 0

while nprint < size**2:
    print(mlist[pos[0]*size+pos[1]], end=" ")
    if pos[0] == size-vdist and pos[1] < hdist:
        pos[1] += 1
    elif pos[1] == dist and pos[0] < vdist:
        pos[0] += 1
    elif pos[0] == vdist and pos[1] > size-hdist:
        pos[1] -= 1
    elif pos[1] == size-hdist and pos[0] > size-hdist:
        pos[0] -= 1
    nprint += 1

'''
pos = [0, 0]
nprint = 0
hdist = size
vdist = size
direc = [0, 1]

while nprint < size**2-1:
    print(mlist[pos[0]*size+pos[1]], end=" ")
    pos = [pos[0]+direc[0], pos[1]+direc[1]]
    nprint += 1


direc = [0, 1]

def changedirec(x):
    if x[1] == hdist and x[0] == size-vdist:
        direc = [-1, 0]
    elif x[1] == 0:
        direc = [1, 0]
    elif x[0] == vdist:
        direc = [0, -1]
    elif x[0] == 0:
        direc = [0, 1]
print(direc)
        
hdist = 5
vdist = 5
'''

changedirec([0, 0])
from random import randint

size = 3 #input("Matrix size? ")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mlist = [alpha[randint(0, 25)] for x in [1]*size**2]
print(mlist)
'''
for x in mlist:
    x = alpha[x-1]
print(mlist)
'''
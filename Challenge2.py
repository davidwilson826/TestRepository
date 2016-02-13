'''
money = int(input("How much money do you have (stop with 0)? "))

hat = 7
shirt = 15
jacket = 23
'''

a = [1,2,3]
b = [1,2,3]
c = [1,2,3]

anew = len(c)*((a*len(b)).sort())
bnew = len(c)*(b*len(a))
cnew = (c*len(a)*len(b)).sort()

abc = zip(anew, bnew, cnew)

print(anew)
print(bnew)
print(cnew)
print(list(abc))
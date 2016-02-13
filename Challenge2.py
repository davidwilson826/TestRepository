'''
money = int(input("How much money do you have (stop with 0)? "))

hat = 7
shirt = 15
jacket = 23
'''

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

for x in abc:
    print(x[0]+x[1]+x[2])
'''

money = 1

while money != 0:
    money = int(input("How much money do you have (stop with 0)? "))

    a = list(range(0,money//7+1))
    b = list(range(0,money//15+1))
    c = list(range(0,money//23+1))

    anew = len(c)*((a*len(b)).sort())
    bnew = len(c)*(b*len(a))
    cnew = (c*len(a)*len(b)).sort()

    abc = zip(anew, bnew, cnew)

    success = "false"

    for x in abc:
        cost = 7*x[0]+15*x[1]+23*x[2]
        if cost == money:
            if success == "false":
                message = "You can spend all your money: "
            else:
                message = "                              "
            print(message+"Hat: "+str(x[0])+" Shirt: "+str(x[1])+" Jacket: "+str(x[2]))
            success = "true"
        
    if success == "false":
        print("You cannot spend all your money!")

    success = "false"

'''
print(anew)
print(bnew)
print(cnew)
print(list(abc))
'''

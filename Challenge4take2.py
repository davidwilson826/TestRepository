
string1 = input("Enter first string? ")
string2 = input("Enter second string? ")

l1 = list(zip(range(0, len(string1)), list(string1)))
l2 = list(zip(range(0, len(string2)), list(string2)))

cstring = ["a"]

for x in l1:
    for y in l2:
        if x[1] == y[1]:
            l1index = l1.index(x)
            l2index = l2.index(y)
            
            currstring = "a"
            
            while l1index <= len(l1)-1 and l2index <= len(l2)-1 and l1[l1index][1] == l2[l2index][1]:
                currstring += l1[l1index][1]
                l1index += 1
                l2index += 1
            
            if (len(currstring[1:]) == len(cstring[-1]) and currstring[1:] != cstring[-1]) or len(cstring) == 1:
                cstring += [currstring[1:]]
            elif len(currstring[1:]) > len(cstring[-1]):
                cstring = ["a", currstring[1:]]
            
if len(cstring) == 1:
    print("#0")
else:
    for x in cstring[1:]:
        print(x+"		#"+str(len(x)))
'''
a = ["a"]
a += ["hello"]
print(a)
'''
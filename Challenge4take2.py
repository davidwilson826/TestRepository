
string1 = "doom"#input("Enter first string? ")
string2 = "dog"#input("Enter second string? ")

l1 = list(zip(range(0, len(string1)), list(string1)))
l2 = list(zip(range(0, len(string2)), list(string2)))

print(l1)
print(l2)

cstring = ["a"]

for x in l1:
    for y in l2:
        if x[1] == y[1]:
            currstring = "a"
            l1index = l1.index(x)
            l2index = l2.index(y)
            
            while l1[l1index][1] == l2[l2index][1] and l1index <= len(l1)-1 and l2index <= len(l2)-1:
                currstring += l1[l1index][1]
                l1index += 1
                l2index += 1
            
            if len(currstring[1:]) == len(cstring[-1]):
                cstring += currstring[1:]
            elif len(currstring[1:]) > len(cstring[-1]):
                cstring = ["a", currstring[1:]]
            
            print(l1index)
            print(l2index)
            
print(cstring)
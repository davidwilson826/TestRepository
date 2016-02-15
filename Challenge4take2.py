string1 = "doom"#input("Enter first string? ")
string2 = "dog"#input("Enter second string? ")

l1 = list(string1)
l2 = list(string2)

print(l1)
print(l2)

for x in l1:
    for y in l2:
        if x == y:
            l1index = l1.index(x)
            l2index = l2.index(y)
            print(l1index)
            print(l2index)
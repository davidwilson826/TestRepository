string1 = input("Enter first string? ")
string2 = input("Enter second string? ")

for x in string1:
    for y in string2:
        if x == y:
            cstring1 = string1[string1.find(x):]
            cstring2 = string2[string2.find(y):]
            print(cstring1)
            print(cstring2)
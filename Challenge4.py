string1 = input("Enter first string? ")
string2 = input("Enter second string? ")

for x in string1:
    for y in string2:
        if x == y:
            cstring1 = string1[x-1:]
            cstring2 = string2[y-1:]
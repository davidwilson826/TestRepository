string1 = input("Enter first string? ")
string2 = input("Enter second string? ")

s1l = list(range(0, len(string1)))
s2l = list(range(0, len(string2)))

for x in string1:
    for y in string2:
        if x == y:
            cstring1 = string1[string1.find(x):]
            cstring2 = string2[string2.find(y):]
            print(cstring1)
            print(cstring2)
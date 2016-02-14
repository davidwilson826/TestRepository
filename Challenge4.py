string1 = "david" #input("Enter first string? ")
string2 = "dog" #input("Enter second string? ")

s1sl = list(string1)
s2sl = list(string2)

s1nl = list(range(0, len(string1)))
s2nl = list(range(0, len(string2)))

s1l = zip(s1sl, s1nl)
s2l = zip(s2sl, s2nl)

for x in s1l:
    for y in s2l:
        if x[1] == y[1]:
            cstring1 = s1l[s1l.find(x):]
            cstring2 = s2l[s2l.find(y):]
            print(cstring1)
            print(cstring2)
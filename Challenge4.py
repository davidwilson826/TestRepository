
string1 = "I am a very big fan of computer science contests" #input("Enter first string? ")
string2 = "I am a big fan of science contests" #input("Enter second string? ")

s1sl = list(string1)
s2sl = list(string2)

s1nl = list(range(0, len(string1)))
s2nl = list(range(0, len(string2)))

s1l = list(zip(s1nl, s1sl))
s2l = list(zip(s2nl, s2sl))

cstring = "a"
currcstring = "a"

for x in s1l:
    for y in s2l:
        if x[1] == y[1]:
            clist1 = s1l[s1l.index(x):]
            clist2 = s2l[s2l.index(y):]

            charnum = 0
            while clist1[charnum][1] == clist2[charnum][1]:
                currcstring += clist1[charnum][1]
                charnum += 1
            if len(currcstring) > len(cstring):
                cstring = currcstring
            currcstring = "a"
            
    print(cstring[1:])

'''
print(clist1)
            print(clist2)
            print(cstring[1:])
            print(charnum)
'''
'''
a = [1,2,3]
b = [1,2,3]

ab = list(zip(a,b))

print(ab[0][1])
'''
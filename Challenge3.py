'''
string = "abcde"

while len(string) > 1:
    string = string[1:]
    print(string)

print("done")


string = input("Enter string (q/Q for stop)?	")

if string[0] == 1:
    output = "a0"
else:
    output = "a"

nextnum = 0

while len(string) > 1:
    if string[0] == 0:
        nextnum += 1
        if string[1] != 0:
            output += " "+str(nextnum)
            nextnum = 0
        string = string[1:]

print(output[1:])
'''
'''
string = input("Enter string (q/Q for stop)?	")

nextnum = 0

while len(string) > 1:
    if string[0] == 0:
        nextnum += 1
    string = string[1:]
    print(string)
    
print("done")
'''

string = "a"

while string != "q" and "Q":
    string = input("Enter string (q/Q for stop)?	")
    if string != "q" and "Q":
        stringorig = string
        nextnum = 0

        if string[0] == "1":
            output = "a 0"
        else:
            output = "a"

        while len(string) > 1:
            nextnum += 1
            if string[0] != string[1]:
                output += " "+str(nextnum)
                nextnum = 0
            string = string[1:]
        
        if string == stringorig[-2] and stringorig[-3] == stringorig[-2]:
            output = output[:-1]+str(int(output[-1])+1)
        elif string == stringorig[-2]:
            output = output+" "+str(int(output[-1])+1)
        else:
            output = output+" 1"
        
        print(output[2:])

string = input("Enter string (q/Q for stop)?	")
print(string[1:])
print(len(string[1:]))

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

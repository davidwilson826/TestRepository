string = input("Enter string (q/Q for stop)?	")

if string[0] == 1:
    output = "0"
    
nextnum = 0

while len(string) > 0:
    if string[0] == 0 and string[1] == 0:
        nextnum += 1
    elif string [0] == 0:
        nextnum += 1
        output += " "+str(nextnum)
        nextnum = 0
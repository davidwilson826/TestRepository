associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

a = 'b"[H\>{0G+I{1(1Hb 15IH >\F3H8]32)JI95263'#input('output: ')
b = 'How now? A rat? Dead, for a ducat, dead!'#input('message: ')

a = [associations.index(x) for x in a]
b = [-1*associations.index(x) for x in b]

print(a)
print(b)

key = [sum(x) for x in zip(a,b)]
print(key)

key = ''.join([associations[x] for x in key])
print(key)

'''
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

a = 'How now? A rat? Dead, for a ducat, dead!'#input('message: ')
b = 'b"[H\>{0G+I{1(1Hb 15IH >\F3H8]32)JI95263'#input('message2: ')

a = [associations.index(x) for x in a]
b = [associations.index(x) for x in b]

print(a)
print(b)
'''

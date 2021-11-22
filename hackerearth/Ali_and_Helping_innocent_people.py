a = input("")

b = list(a)
c = ['A', 'E', 'I', 'O', 'U', 'Y']
d = int(b[0])+int(b[1])

e = int(b[3])+int(b[4])

f = int(b[4])+int(b[5])

g = int(b[7])+int(b[8])

if b[2] not in c and d%2==0 and e%2==0 and f%2==0 and g%2==0 and b[6]=='-' and len(b)==9:
    print("valid")
else:
    print("invalid")

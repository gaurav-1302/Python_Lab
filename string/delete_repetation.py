s = input()
l = s.split()
k = []
for i in l:
 
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))
    

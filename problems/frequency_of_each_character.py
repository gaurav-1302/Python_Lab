#find the frequency of each character
a = input("enter string ")
b = ''
for i in a:
	if i not in b:
		
		print(i, a.count(i))
		b = b+i

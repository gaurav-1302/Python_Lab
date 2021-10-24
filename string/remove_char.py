a = input("enter the string: ")
c = ""
for i in a:
    if i.isalpha():
        c = "".join([c,i])
print("final string with only characters ",c)

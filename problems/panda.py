from itertools import permutations
n = int(input("enter the number of peaces: "))
ai = list(input("reprsent piece without cherry (0) and with cherry (1) :"))
if n==len(ai):
    print(ai)
    x= permutations(ai)
    for i in list(x):
        print(i)
        

else:
    print("error")




